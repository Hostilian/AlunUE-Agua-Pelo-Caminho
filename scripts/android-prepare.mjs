// Capacitor's official CLI supplies the native shell. Keep web sources in dist/.
import {cp, mkdir, readdir, readFile, writeFile, rm} from 'node:fs/promises';
import {fileURLToPath} from 'node:url';
import path from 'node:path';
import {createRequire} from 'node:module';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const stage = path.join(root, 'android-shell', 'www');
const source = path.join(root, 'dist');
const publicOrigin = 'https://hostilian.github.io/AlunUE-Agua-Pelo-Caminho/';
const require = createRequire(path.join(root, 'android-shell', 'package.json'));
const {build} = require('esbuild');
if (path.dirname(stage) !== path.join(root, 'android-shell')) throw Error('Invalid staging directory');
await rm(stage, {recursive: true, force: true});
await mkdir(stage, {recursive: true});
await cp(source, stage, {
  recursive: true,
  filter: file => !/\.(?:apk|aab|pdf|md)$/i.test(file)
});
// Android WebView does not display PDF/Markdown downloads. Keep these links on
// the published HTTPS origin; the independent website/report stay unchanged.
async function htmlFiles(directory) {
  const found = [];
  for (const entry of await readdir(directory, {withFileTypes: true})) {
    const file = path.join(directory, entry.name);
    if (entry.isDirectory()) found.push(...await htmlFiles(file));
    else if (entry.name.endsWith('.html')) found.push(file);
  }
  return found;
}
for (const file of await htmlFiles(stage)) {
  const page = path.relative(stage, file).replaceAll(path.sep, '/');
  const html = await readFile(file, 'utf8');
  const entryScript = /<script type="module" src="(?:app|investigacao)\.mjs(?:\?[^"\s]*)?">/;
  if (['index.html', 'investigacao.html'].includes(page) && !entryScript.test(html)) {
    throw Error(`Android staging could not locate the ${page} module entrypoint.`);
  }
  let nativeHtml = html.replace(
    /href="((?!https?:|#|\/)[^"\s]+\.(?:pdf|md|apk)(?:\?[^"\s]*)?)"/g,
    (_, relative) => `href="${new URL(relative, new URL(page, publicOrigin)).href}" target="_blank" rel="noopener"`
  ).replace(entryScript, match => '<script type="module" src="native-bridge.mjs"></script>' + match);
  if (page === 'novidades.html') {
    nativeHtml = nativeHtml.replace(/<h3>Android para testes<\/h3><p>[\s\S]*?<\/p>/,
      '<h3>Android para testes</h3><p>Estás a usar uma versão Android de teste. A validação num dispositivo continua necessária. <a href="' + publicOrigin + 'novidades.html" target="_blank" rel="noopener">Consulta as versões, transferências e verificações mais recentes na página pública ↗</a>.</p>');
  }
  await writeFile(file, nativeHtml);
}
await build({
  entryPoints: [path.join(root, 'android-shell', 'native-bridge.mjs')],
  bundle: true,
  format: 'esm',
  platform: 'browser',
  target: 'chrome100',
  outfile: path.join(stage, 'native-bridge.mjs'),
  legalComments: 'linked'
});
await cp(path.join(root, 'android-shell', 'node_modules', '@capacitor', 'core', 'LICENSE'), path.join(stage, 'CAPACITOR-LICENSE.txt'));
await cp(path.join(root, 'android-shell', 'LICENSE-IONIC-PLUGINS.txt'), path.join(stage, 'IONIC-PLUGINS-LICENSE.txt'));
console.log('Android web assets staged from dist/; reports/docs use public HTTPS links.');
