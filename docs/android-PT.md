# Android · AlunUÉ Água

## Compilação verificada · 31 de outubro de 2026

Foi produzido o APK de teste `dist/downloads/AlunUE-Android-Teste.apk`, com **5 996 270 bytes**. A compilação local concluiu com sucesso e a ferramenta oficial apksigner confirmou a assinatura de depuração no esquema APK v2. AAPT confirmou a identidade `pt.alunue.aguapelocaminho`, versão `0.1.0-teste`, mínimo API 24 e alvo API 36, com hardware de localização opcional.

SHA-256:

```text
29de661731ea942c85159702227d2bf44c80e7d9f557f8dbfd98c70c3777b7c3
```

Os módulos web empacotados foram comparados com os ficheiros atuais de `dist/`. Os adaptadores nativos estão presentes nas páginas da aplicação e de investigação; a página de novidades está incluída e aponta para atualizações públicas. Não há APK recursivamente empacotado nem chaves privadas no ficheiro. O relatório da fase 1 manteve a soma SHA-256 original.

**Não foi instalado nem testado num dispositivo ou emulador**: não havia um dispositivo ADB ligado nem um emulador configurado. Partilha, permissões, ciclo de vida, TalkBack e comportamento visual nativo continuam na checklist de validação. Não existe uma assinatura de lançamento ou publicação numa loja.

## Implementação

Invólucro nativo com o Capacitor 8.6.0, gerado pelo CLI oficial, reutilizando a aplicação estática de `dist/`. O pacote é `pt.alunue.aguapelocaminho`, com nome visível **AlunUÉ Água** e versão **0.1.0-teste**. A estrutura fica isolada em `android-shell/`; o website continua sem dependências npm de execução.

O projeto usa Android API 36 para compilação/alvo e suporta API 24 ou superior. É necessário um Android System WebView atualizado. O Gradle Wrapper tem a distribuição oficial e uma soma SHA-256 fixada. A chave de depuração é gerida pelo SDK e não pertence ao repositório. Não há chave de lançamento nem publicação numa loja.

## Compilar no Windows

Pré-requisitos: Node 22+, JDK 21 (incluído no Android Studio), Android SDK 36 e build-tools instalados/licenciados. As dependências npm estão fixadas num lockfile.

Na raiz do repositório:

```powershell
.\scripts\android-build.ps1 -InstallDependencies
```

Também é possível usar os comandos equivalentes em `android-shell/`:

```powershell
npm ci
npm run sync
.\android\gradlew.bat -p android assembleDebug --no-daemon
```

`JAVA_HOME` deve indicar o JDK 21 e `android/local.properties` deve indicar o SDK. O script aceita `-AndroidSdkPath` e `-JavaPath`, configura apenas o processo atual e cria caches locais ignoradas pelo Git. Também usa `android-shell/.tmp` como TEMP/TMP do processo para evitar falhas de sockets locais do Java em alguns executores Windows. Não altera as definições globais do sistema.

Resultado esperado: `android-shell/output/AlunUE-Agua-0.1.0-teste.apk` e ficheiro SHA-256. A compilação inclui verificação da assinatura de depuração e leitura do manifesto com as ferramentas oficiais Android. Uma assinatura válida de depuração permite testes; não é uma versão de produção.

## Adaptações para Android

- A interface e o inventário cartográfico inicial são empacotados no APK. Não é necessário carregar o website para abrir a interface. As APIs, os mosaicos de mapa opcionais e a navegação externa exigem internet.
- O mapa estático continua disponível quando o serviço externo falha. Os candidatos mantêm o estado não verificado.
- O User-Agent identifica a aplicação AlunUEAgua e o website público.
- O adaptador nativo usa os plugins oficiais Geolocation, Share e Filesystem. Só pede **localização aproximada em primeiro plano**, após a pessoa tocar no botão de localização. O início manual continua disponível. Não há rastreamento em segundo plano.
- Partilhar abre a folha de partilha do Android. Guardar em texto e exportar a investigação criam ficheiros TXT, JSON ou CSV na subpasta `exports` da cache privada e abrem a folha de partilha para escolher onde guardar/enviar. Os nomes são validados para impedir caminhos arbitrários. A cache pode ser removida pelo sistema; guardar uma cópia no destino escolhido. A ação de apagar dados locais também remove esses ficheiros de exportação.
- Sem permissões gerais de armazenamento, câmara, microfone, contactos, notificações ou localização em segundo plano. Cópias de segurança automáticas da aplicação estão desativadas.
- O manifesto compilado inclui INTERNET, ACCESS_COARSE_LOCATION, ACCESS_NETWORK_STATE e uma permissão interna de recetores AndroidX protegida por assinatura. A localização é opcional também como requisito de hardware; o início manual permite usar a aplicação sem esse recurso.
- Os relatórios e documentos ligados abrem a versão HTTPS pública, porque o Android WebView não apresenta esses downloads como páginas HTML. O relatório submetido na fase 1 não é alterado.
- Ícone vetorial adapta a gota do projeto. O tratamento de margens das barras do sistema usa o mecanismo nativo do Capacitor.

## Instalar e validar

O workflow manual **Compilar Android de teste**, em `.github/workflows/android.yml`, permite compilar num runner Ubuntu com os SDKs oficiais quando o ambiente local não tem conectividade suficiente. Não é executado automaticamente nem publica numa loja. O artefacto contém o APK de depuração, SHA-256, identificação do commit e resultados da verificação da assinatura e do manifesto. As chaves de depuração não são incluídas no artefacto.

Usar um dispositivo de teste ou emulador que o utilizador controla. A instalação manual de um APK deve ser iniciada conscientemente pelo utilizador; não há instalação automática em dispositivos pessoais.

Para desenvolvimento com dispositivo/emulador autorizado:

```powershell
adb install -r android-shell/output/AlunUE-Agua-0.1.0-teste.apk
```

Checklist antes de distribuir como produto:

1. Arranque limpo, orientação e margens do sistema; pesquisa e filtros em português; três estados de confiança distintos.
2. Recusar a localização e concluir o percurso com início manual. Permitir apenas a localização aproximada; verificar retorno à aplicação.
3. Selecionar, reordenar e retirar paragens; abrir todas as partes do Google Maps.
4. Copiar, partilhar, cancelar a partilha e guardar o texto. Abrir o ficheiro guardado e confirmar todas as paragens.
5. Ativar modo de avião; abrir a interface empacotada; confirmar erros claros nas consultas e o mapa estático.
6. Apagar os dados locais e confirmar remoção da cache de exportação. Consultar permissões Android.
7. Testar com TalkBack, tamanho de letra ampliado e controlos por teclado/comutador quando disponíveis.
8. Rever os pontos de água no terreno e realizar os testes com utilizadores previstos; um APK não valida esses dados.

O sucesso da compilação não demonstra estas verificações num dispositivo. O estado efetivamente verificado e o SHA do APK são registados no resumo de compilação entregue com o artefacto.

## Fontes oficiais

- [Adicionar Capacitor a uma aplicação existente](https://capacitorjs.com/docs/getting-started).
- [Ambiente de desenvolvimento](https://capacitorjs.com/docs/getting-started/environment-setup).
- [Android](https://capacitorjs.com/docs/android), [configuração](https://capacitorjs.com/docs/config) e [barras do sistema](https://capacitorjs.com/docs/apis/system-bars).
- [Geolocation](https://capacitorjs.com/docs/apis/geolocation), [Share](https://capacitorjs.com/docs/apis/share), [Filesystem](https://capacitorjs.com/docs/apis/filesystem).
- [Compilar e assinar uma versão de depuração](https://developer.android.com/build/building-cmdline).

Consulta das fontes e preparação: 30 de outubro de 2026. Créditos adicionais em `android-shell/THIRD_PARTY_NOTICES.md`.
