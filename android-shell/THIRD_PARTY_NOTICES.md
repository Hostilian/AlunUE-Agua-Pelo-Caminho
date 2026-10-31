# Código e ferramentas reutilizados

O projeto Android foi gerado pelo CLI oficial do Capacitor; não foi copiado um projeto arbitrário. A interface web existente é reutilizada como recurso local do APK.

| Componente | Versão fixada | Licença / origem |
|---|---|---|
| Capacitor core, Android e CLI | 8.6.0 | MIT, Drifty Co., https://github.com/ionic-team/capacitor |
| Capacitor Geolocation | 8.2.4 | MIT, https://github.com/ionic-team/capacitor-geolocation |
| Capacitor Share | 8.0.3 | MIT, https://github.com/ionic-team/capacitor-plugins |
| Capacitor Filesystem | 8.1.5 | MIT, https://github.com/ionic-team/capacitor-filesystem |
| esbuild, apenas compilação | 0.28.2 | MIT, https://github.com/evanw/esbuild |
| Gradle Wrapper | 8.14.3 | Apache-2.0, https://gradle.org/ |

As versões efetivas e dependências transitivas estão no package-lock.json. LICENSE-CAPACITOR.txt e LICENSE-IONIC-PLUGINS.txt preservam os avisos MIT; ambos são incluídos nos recursos web do APK. O empacotador preserva comentários legais. O código específico do projeto continua com a licença indicada pelo repositório principal.

O mapa e os dados continuam sujeitos aos créditos e licenças apresentados na aplicação; a criação de um APK não altera esses requisitos.
