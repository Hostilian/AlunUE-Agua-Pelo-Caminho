import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import fs from 'node:fs';

const source=fs.readFileSync(new URL('../dist/sw.js',import.meta.url),'utf8');
function worker({match=async()=>undefined}={}){
  const handlers={};
  const scope={URL,Response,fetch:async()=>{throw Error('offline');},caches:{match},self:{location:{origin:'https://example.test',href:'https://example.test/alunue/sw.js'},addEventListener:(name,fn)=>{handlers[name]=fn;}}};
  vm.runInNewContext(source,scope);
  return handlers;
}
test('offline navigation recovers a cached page despite a release query',async()=>{
  let options,response;
  const handlers=worker({match:async(_request,opts)=>{options=opts;return new Response('saved application');}});
  handlers.fetch({request:{url:'https://example.test/alunue/index.html?review=release6',method:'GET'},respondWith:p=>{response=p;}});
  assert.equal(await(await response).text(),'saved application');
  assert.equal(options.ignoreSearch,true);
});
test('external map tiles and provider APIs are never intercepted or cached by the shell',()=>{
  const handlers=worker();let intercepted=false;
  for(const url of ['https://tile.openstreetmap.org/16/31328/25144.png','https://api.open-meteo.com/v1/forecast'])handlers.fetch({request:{url,method:'GET'},respondWith:()=>{intercepted=true;}});
  assert.equal(intercepted,false);
});
test('first-use offline failure explains recovery and returns a failure status',async()=>{
  let response;
  worker().fetch({request:{url:'https://example.test/alunue/index.html',method:'GET'},respondWith:p=>{response=p;}});
  const result=await response;assert.equal(result.status,503);assert.match(await result.text(),/Liga-te à internet/);
});
