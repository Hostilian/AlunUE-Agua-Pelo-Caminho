import fs from 'node:fs';import path from 'node:path';import assert from 'node:assert/strict';import {fileURLToPath} from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..'),dist=path.join(root,'dist');const html=fs.readFileSync(path.join(dist,'index.html'),'utf8');
for(const m of html.matchAll(/(?:src|href)="([^"#]+)"/g)){const value=m[1];if(!/^(https?:|data:)/.test(value))assert.ok(fs.existsSync(path.join(dist,value)),`Missing asset ${value}`);}
const manifest=JSON.parse(fs.readFileSync(path.join(dist,'manifest.webmanifest')));assert.equal(manifest.display,'standalone');assert.ok(/demonstração/i.test(html));assert.equal(manifest.lang,'pt-PT');assert.ok(html.includes('lang="pt-PT"'));
for(const f of ['core.mjs','api.mjs','app.mjs','sw.js','style.css','project-plan.md','api-contracts.md'])assert.ok(fs.statSync(path.join(dist,f)).size>0);
console.log('Local asset links, manifest and required project files passed.');
