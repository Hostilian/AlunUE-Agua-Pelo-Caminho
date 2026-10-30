from pathlib import Path
import json,math
from reportlab.graphics.shapes import Drawing,Rect,Line,Circle,String,Polygon,PolyLine
from reportlab.lib.colors import HexColor,white

R=Path(__file__).parent
def build_map(en=False):
    data=json.loads((R/'evora-osm.json').read_text(encoding='utf-8'));es=data['elements']
    d=Drawing(495,230)
    C=lambda value:HexColor(value)
    d.add(Rect(0,24,495,202,rx=10,ry=10,fillColor=C('#F1F3E9'),strokeColor=None))
    west,south,east,north=-7.916,38.565,-7.899,38.5765
    k=111320;cos=math.cos(math.radians((south+north)/2));scale=min(236/((east-west)*k*cos),186/((north-south)*k))
    mw=(east-west)*k*cos*scale;mh=(north-south)*k*scale;x0=130+(236-mw)/2;y0=31+(186-mh)/2
    def xy(p):return (x0+(p['lon']-west)*k*cos*scale,y0+(p['lat']-south)*k*scale)
    def inside(p):return west<=p['lon']<=east and south<=p['lat']<=north
    def poly(e,fill):
        geom=e.get('geometry',[])
        if len(geom)>2 and all(inside(p) for p in geom):d.add(Polygon([v for p in geom for v in xy(p)],fillColor=C(fill),strokeColor=None))
    for e in es:
        tags=e.get('tags',{})
        if tags.get('leisure') in ['park','garden'] or tags.get('landuse') in ['grass','forest']:poly(e,'#C9DFC5')
        elif 'building' in tags:poly(e,'#D8D4C8')
    # Keep geometry in its true projection; do not stretch the centre to fit the banner.
    roads=[e for e in es if 'highway' in e.get('tags',{}) and len(e.get('geometry',[]))>1]
    def segments(geom):
        current=[]
        for p in geom:
            if inside(p):current.append(xy(p))
            else:
                if len(current)>1:yield current
                current=[]
        if len(current)>1:yield current
    for layer in [0,1]:
        for e in roads:
            kind=e['tags']['highway'];width={'primary':2.2,'secondary':2,'tertiary':1.7,'residential':1.15,'pedestrian':1.0,'living_street':.9,'service':.65,'footway':.45,'path':.4,'steps':.35}.get(kind,.55)
            for seg in segments(e['geometry']):d.add(PolyLine([v for p in seg for v in p],strokeColor=white if layer==0 else C('#A9B5AC'),strokeWidth=width+.65 if layer==0 else width,fillColor=None))
    for e in es:
        if e.get('tags',{}).get('historic')=='citywalls' or e.get('tags',{}).get('barrier')=='city_wall':
            for seg in segments(e.get('geometry',[])):d.add(PolyLine([v for p in seg for v in p],strokeColor=C('#B97A56'),strokeWidth=1.35,fillColor=None))
    waters=[]
    for e in es:
        if e.get('tags',{}).get('amenity')=='drinking_water' and 'lat' in e and inside(e):
            if not any(math.hypot((e['lon']-p['lon'])*k*cos,(e['lat']-p['lat'])*k)<15 for p in waters):waters.append(e)
    for p in waters:
        x,y=xy(p);d.add(Circle(x,y,2.9,fillColor=white,strokeColor=C('#277F9E'),strokeWidth=1.0))
    refs={e['id']:e for e in es if e['type']=='way'}
    landmarks=[(221910079,'Praça de Giraldo',8,126,'#246D64'),(92158127,'Templo Romano',377,170,'#A85631'),(857661406,'Jardim Público',8,72,'#53649A'),(674094950,'Colégio do Espírito Santo',377,111,'#246D64')]
    for i,(ident,label,lx,ly,col) in enumerate(landmarks,1):
        e=refs[ident];g=e['geometry'];point={'lat':sum(p['lat'] for p in g)/len(g),'lon':sum(p['lon'] for p in g)/len(g)};x,y=xy(point)
        endx=lx+111 if lx<130 else lx;d.add(Line(x,y,endx,ly+12,strokeColor=C(col),strokeWidth=.7))
        d.add(Rect(lx,ly-5,111,37,rx=5,ry=5,fillColor=white,strokeColor=None))
        d.add(Circle(x,y,5.6,fillColor=C(col),strokeColor=white,strokeWidth=.6));d.add(String(x,y-2,str(i),fontName='ArialBold',fontSize=6.7,textAnchor='middle',fillColor=white))
        # Two-line campus label avoids crowding the map.
        labels=['Colégio do Espírito','Santo · UÉ'] if i==4 else [label]
        for j,line in enumerate(labels):d.add(String(lx+7,ly+15-j*11,line,fontName='ArialBold',fontSize=7.6,fillColor=C(col)))
    d.add(String(8,205,'ÉVORA',fontName='ArialBold',fontSize=18,fillColor=C('#17493E')))
    d.add(String(8,190,'Historic centre' if en else 'Centro histórico',fontName='Arial',fontSize=8.8,fillColor=C('#52665E')))
    d.add(String(8,175,'OSM street geometry' if en else 'Geometria real OSM',fontName='Arial',fontSize=7.5,fillColor=C('#52665E')))
    d.add(String(377,66,f'{len(waters)} OSM water candidates' if en else f'{len(waters)} candidatos OSM',fontName='ArialBold',fontSize=7.4,fillColor=C('#277F9E')))
    d.add(String(377,54,'Not checked on site' if en else 'Não verificados no local',fontName='Arial',fontSize=7,fillColor=C('#52665E')))
    d.add(String(377,42,'No route is shown' if en else 'Não representa um itinerário',fontName='Arial',fontSize=6.8,fillColor=C('#52665E')))
    sx,sy=x0+9,y0+9;d.add(Rect(sx-3,sy-4,200*scale+8,18,fillColor=white,strokeColor=None));d.add(Line(sx,sy, sx+200*scale,sy,strokeColor=C('#17493E'),strokeWidth=1.5));d.add(String(sx,sy+5,'200 m',fontName='Arial',fontSize=6.5,fillColor=C('#17493E')))
    d.add(Line(x0+mw-10,y0+mh-30,x0+mw-10,y0+mh-13,strokeColor=C('#17493E'),strokeWidth=1.1));d.add(String(x0+mw-10,y0+mh-9,'N',fontName='ArialBold',fontSize=7,textAnchor='middle',fillColor=C('#17493E')))
    d.add(String(0,12,'© OpenStreetMap contributors · ODbL · 30/10/2026 · openstreetmap.org/copyright',fontName='Arial',fontSize=6.6,fillColor=C('#52665E')))
    d.add(String(0,1,'Map listings do not confirm free access, potability or operation.' if en else 'Os registos cartográficos não confirmam acesso gratuito, potabilidade ou funcionamento.',fontName='Arial',fontSize=7.1,fillColor=C('#52665E')))
    return d
