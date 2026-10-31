// Thin Android adapter around official Capacitor APIs; web app stays browser-first.
// API examples: https://capacitorjs.com/docs/apis/{geolocation,share,filesystem}
import {Capacitor} from '@capacitor/core';
import {Geolocation} from '@capacitor/geolocation';
import {Share} from '@capacitor/share';
import {Directory, Encoding, Filesystem} from '@capacitor/filesystem';

function sharingError(error) {
  return /cancel|dismiss/i.test(error?.message || '')
    ? new DOMException('Partilha cancelada.', 'AbortError') : error;
}

if (Capacitor.isNativePlatform()) {
  Object.defineProperty(navigator, 'geolocation', {
    configurable: true,
    value: {
      getCurrentPosition(success, failure, options = {}) {
        // Called only by the existing explicit location button. Approximate,
        // foreground permission is sufficient; never request background access.
        (async () => {
          let permission = await Geolocation.checkPermissions();
          if (permission.coarseLocation !== 'granted') {
            permission = await Geolocation.requestPermissions({permissions: ['coarseLocation']});
          }
          if (permission.coarseLocation !== 'granted') {
            const error = new Error('Localização não autorizada. Escolhe um início manual.');
            error.code = 1;
            throw error;
          }
          return Geolocation.getCurrentPosition({
            enableHighAccuracy: false,
            timeout: options.timeout || 10000,
            maximumAge: options.maximumAge || 60000
          });
        })().then(success).catch(error => failure?.({
          code: typeof error.code === 'number' ? error.code : 2,
          message: error.message || 'Localização indisponível.'
        }));
      }
    }
  });

  Object.defineProperty(navigator, 'share', {
    configurable: true,
    value: async ({title, text, url} = {}) => {
      try {
        await Share.share({title, text, url, dialogTitle: 'Partilhar percurso AlunUÉ'});
      } catch (error) { throw sharingError(error); }
    }
  });

  window.AlunUENative = Object.freeze({
    async clearExports() {
      try {
        await Filesystem.rmdir({path: 'exports', directory: Directory.Cache, recursive: true});
      } catch (error) {
        // A first visit has no exported file to remove.
        if (!/not exist|not found|ENOENT/i.test(error?.message || '')) throw error;
      }
    },
    async saveText(text, filename = 'alunue-percurso.txt') {
      if (!/^[a-zA-Z0-9][a-zA-Z0-9._-]{0,79}\.(?:txt|json|csv)$/.test(filename) || filename.includes('..')) {
        throw new Error('Nome de exportação inválido. Usa TXT, JSON ou CSV.');
      }
      const result = await Filesystem.writeFile({
        path: `exports/${filename}`,
        data: String(text),
        directory: Directory.Cache,
        encoding: Encoding.UTF8,
        recursive: true
      });
      try {
        await Share.share({
          title: 'Exportação AlunUÉ',
          files: [result.uri],
          dialogTitle: 'Guardar ou partilhar ficheiro'
        });
      } catch (error) { throw sharingError(error); }
    }
  });
}
