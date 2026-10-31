// Uses Leaflet's official quick-start pattern. Vendored Leaflet: BSD-2-Clause.
// https://leafletjs.com/examples/quick-start/ — see vendor/leaflet/LICENSE.
import {validCoordinate} from './core.mjs?v=6';

const TILE_URL = 'https://tile.openstreetmap.org/{z}/{x}/{y}.png';
const LANDMARKS = [
  {name:'Praça de Giraldo',symbol:'G',lat:38.5708538,lon:-7.9094566,way:221910079},
  {name:'Templo Romano',symbol:'T',lat:38.5726102,lon:-7.9073393,way:92158127},
  {name:'Jardim Público',symbol:'J',lat:38.5675376,lon:-7.9108365,way:857661406},
  {name:'Colégio do Espírito Santo · UÉ',symbol:'UÉ',lat:38.5736388,lon:-7.9044345,way:674094950}
];

function leafletReady() {
  if (window.L) return Promise.resolve(window.L);
  const css = document.createElement('link');
  css.rel = 'stylesheet';
  css.href = new URL('./vendor/leaflet/leaflet.css',import.meta.url).href;
  document.head.append(css);
  return new Promise((resolve,reject)=>{
    const script = document.createElement('script');
    const timer = setTimeout(()=>reject(Error('Biblioteca indisponível.')),10000);
    script.src = new URL('./vendor/leaflet/leaflet.js',import.meta.url).href;
    script.onload = ()=>{clearTimeout(timer);window.L?resolve(window.L):reject(Error('Mapa indisponível.'));};
    script.onerror = ()=>{clearTimeout(timer);script.remove();css.remove();reject(Error('Biblioteca indisponível.'));};
    document.head.append(script);
  });
}

function text(tag,value,className) {
  const node=document.createElement(tag);
  node.textContent=value;
  if(className) node.className=className;
  return node;
}

export function initInteractiveMap({getPoints,onSelect,onOrigin}) {
  const open=document.querySelector('#map-open');
  const canvas=document.querySelector('#street-map');
  const status=document.querySelector('#map-status');
  const reset=document.querySelector('#map-reset');
  const choose=document.querySelector('#map-choose-origin');
  if(!open||!canvas||!status) return {refresh(){}};
  let map,pointsLayer,L,loading=false,choosing=false;
  open.hidden=false;

  function renderPoints() {
    if(!map) return;
    pointsLayer.clearLayers();
    const points=getPoints().filter(p=>!p.demo&&validCoordinate(p));
    points.forEach((point,index)=>{
      const water=point.kind==='water';
      const title=`${point.name} · ${water?'água por verificar':'referência por confirmar'}`;
      const marker=L.marker([point.lat,point.lon],{
        icon:L.divIcon({className:`map-pin ${water?'map-pin-water':'map-pin-place'}`,html:`<span>${index+1}</span>`,iconSize:[32,32],iconAnchor:[16,16]}),
        title,alt:title,keyboard:true,riseOnHover:true
      }).addTo(pointsLayer);
      marker.getElement().setAttribute('aria-label',title);
      const popup=document.createElement('div');
      popup.className='map-popup';
      popup.append(text('strong',point.name));
      popup.append(text('p',water?'Candidato cartográfico. Potabilidade, funcionamento, acesso e gratuitidade não confirmados.':'Referência cartográfica. Confirma o acesso e os horários antes de sair.'));
      popup.append(text('p',point.sourceLabel||'Fonte: OpenStreetMap / Wikipédia.','fine'));
      const show=text('button','Ver na lista');
      show.type='button';
      show.addEventListener('click',()=>{map.closePopup();onSelect(point);});
      const close=text('button','Fechar detalhes');
      close.type='button';
      close.addEventListener('click',()=>map.closePopup());
      popup.append(show,close);
      marker.bindPopup(popup,{closeButton:false,maxWidth:300});
    });
    for(const landmark of LANDMARKS) {
      const marker=L.marker([landmark.lat,landmark.lon],{
        icon:L.divIcon({className:'map-pin map-pin-landmark',html:`<span>${landmark.symbol}</span>`,iconSize:[32,32],iconAnchor:[16,16]}),
        title:landmark.name,alt:landmark.name,keyboard:true
      }).addTo(pointsLayer);
      marker.getElement().setAttribute('aria-label',landmark.name);
      const popup=document.createElement('div');
      popup.append(text('strong',landmark.name),text('p','Referência de orientação; não identifica um ponto de água.'));
      const link=text('a','Consultar referência no OpenStreetMap ↗');
      link.href=`https://www.openstreetmap.org/way/${landmark.way}`;
      link.target='_blank';link.rel='noopener';popup.append(link);
      const close=text('button','Fechar detalhes');close.type='button';
      close.addEventListener('click',()=>map.closePopup());popup.append(close);
      marker.bindPopup(popup,{maxWidth:280,closeButton:false});
    }
    document.querySelector('#map-legend-count').textContent=String(points.filter(p=>p.kind==='water').length);
  }

  open.addEventListener('click',async()=>{
    if(loading) return;
    if(map) {
      canvas.hidden=!canvas.hidden;
      open.textContent=canvas.hidden?'Mostrar mapa interativo':'Ocultar mapa interativo';
      open.setAttribute('aria-expanded',String(!canvas.hidden));
      reset.hidden=canvas.hidden;
      choose.hidden=canvas.hidden;
      if(!canvas.hidden) map.invalidateSize();
      return;
    }
    loading=true;open.disabled=true;
    status.textContent='A abrir o mapa. A lista e o mapa estático continuam disponíveis.';
    try {
      L=await leafletReady();canvas.hidden=false;
      map=L.map(canvas,{scrollWheelZoom:false,zoomControl:false,minZoom:13,maxZoom:19,zoomAnimation:!matchMedia('(prefers-reduced-motion: reduce)').matches,fadeAnimation:!matchMedia('(prefers-reduced-motion: reduce)').matches});
      map.attributionControl.setPrefix('<a href="https://leafletjs.com/" title="Biblioteca de mapas interativos">Leaflet</a>');
      map.setView([38.5708,-7.9080],16);
      const zoom=L.control.zoom({zoomInTitle:'Aproximar',zoomOutTitle:'Afastar'}).addTo(map);
      zoom.getContainer().querySelector('.leaflet-control-zoom-in').setAttribute('aria-label','Aproximar mapa');
      zoom.getContainer().querySelector('.leaflet-control-zoom-out').setAttribute('aria-label','Afastar mapa');
      L.control.scale({imperial:false,position:'bottomleft'}).addTo(map);
      const tiles=L.tileLayer(TILE_URL,{
        attribution:'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap contributors</a> · ODbL',
        maxZoom:19,updateWhenIdle:true,keepBuffer:1
      });
      let failed=false;tiles.on('loading',()=>{failed=false;});
      tiles.on('tileerror',()=>{
        failed=true;
        status.textContent='Algumas ruas não carregaram. Consulta o mapa estático acima e a lista; os candidatos continuam por verificar.';
      });
      tiles.on('load',()=>{
        if(!failed) status.textContent='Mapa aberto. Usa +/− para ampliar e as setas para mover quando o mapa tem foco. A lista oferece os mesmos candidatos.';
      });
      tiles.addTo(map);
      pointsLayer=L.layerGroup().addTo(map);renderPoints();
      reset.hidden=false;
      choose.hidden=false;
      choose.addEventListener('click',()=>{
        choosing=!choosing;choose.setAttribute('aria-pressed',String(choosing));
        status.textContent=choosing?'Toca numa rua do mapa para definir o início, ou prime novamente este botão para cancelar.':'Escolha do início cancelada. O início anterior foi mantido.';
      });
      map.on('click',event=>{
        if(!choosing)return;
        onOrigin({lat:event.latlng.lat,lon:event.latlng.lng});
        choosing=false;choose.setAttribute('aria-pressed','false');
        status.textContent='Início definido no mapa. Consulta O meu percurso para rever as coordenadas e as paragens.';
      });
      reset.addEventListener('click',()=>map.setView([38.5708,-7.9080],16,{animate:false}));
      open.textContent='Ocultar mapa interativo';open.setAttribute('aria-expanded','true');
      status.textContent='Mapa aberto. A carregar as ruas; os candidatos não representam água garantida.';
    } catch {
      map?.remove();map=null;canvas.hidden=true;
      status.textContent='Mapa interativo indisponível. Continua com o mapa estático, a pesquisa e a lista de locais.';
      open.textContent='Tentar abrir o mapa';
    } finally {loading=false;open.disabled=false;}
  });
  return {refresh:renderPoints};
}
