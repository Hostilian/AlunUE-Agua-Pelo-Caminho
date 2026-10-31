param(
    [string]$AndroidSdkPath = $env:ANDROID_HOME,
    [string]$JavaPath,
    [switch]$InstallDependencies
)
$ErrorActionPreference = 'Stop'
$projectRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$nativeRoot = Join-Path $projectRoot 'android-shell'
if (-not $AndroidSdkPath) { $AndroidSdkPath = Join-Path $env:LOCALAPPDATA 'Android\Sdk' }
if (-not (Test-Path -LiteralPath (Join-Path $AndroidSdkPath 'platforms\android-36'))) {
    throw 'Instala a plataforma Android SDK 36 e indica -AndroidSdkPath.'
}
if (-not $JavaPath) { $JavaPath = Join-Path $env:ProgramFiles 'Android\Android Studio\jbr' }
if (-not (Test-Path -LiteralPath (Join-Path $JavaPath 'bin\java.exe'))) { $JavaPath = $env:JAVA_HOME }
if (-not $JavaPath) { throw 'Indica -JavaPath para um JDK 21.' }
$env:JAVA_HOME = $JavaPath
$env:ANDROID_HOME = $AndroidSdkPath
$env:GRADLE_USER_HOME = Join-Path $nativeRoot '.gradle-user'
$temporaryRoot = Join-Path $nativeRoot '.tmp'
New-Item -Path $temporaryRoot -ItemType Directory -Force | Out-Null
# Native Windows paths avoid AF_UNIX selector failures in packaged app runners.
# These variables affect this build process and its children, not Windows settings.
$env:TEMP = $temporaryRoot
$env:TMP = $temporaryRoot
$sdkProperty = 'sdk.dir=' + $AndroidSdkPath.Replace('\', '/')
Set-Content -LiteralPath (Join-Path $nativeRoot 'android\local.properties') -Value $sdkProperty -Encoding ascii

Push-Location -LiteralPath $nativeRoot
try {
    if ($InstallDependencies -or -not (Test-Path -LiteralPath 'node_modules\@capacitor\core')) {
        npm ci --no-audit --no-fund --cache .npm-cache
        if ($LASTEXITCODE -ne 0) { throw 'A instalação das dependências falhou.' }
    }
    npm run sync
    if ($LASTEXITCODE -ne 0) { throw 'A sincronização Capacitor falhou.' }
    & '.\android\gradlew.bat' -p android assembleDebug --no-daemon --console plain
    if ($LASTEXITCODE -ne 0) { throw 'A compilação Android falhou.' }
    $apk = Join-Path $nativeRoot 'android\app\build\outputs\apk\debug\app-debug.apk'
    $buildTools = Get-ChildItem -LiteralPath (Join-Path $AndroidSdkPath 'build-tools') -Directory |
        Where-Object { $_.Name -match '^\d+\.\d+\.\d+$' } |
        Sort-Object { [version]$_.Name } -Descending | Select-Object -First 1
    if (-not $buildTools) { throw 'Android build-tools não encontrados.' }
    $artifactRoot = Join-Path $nativeRoot 'output'
    New-Item -Path $artifactRoot -ItemType Directory -Force | Out-Null
    & (Join-Path $buildTools.FullName 'apksigner.bat') verify --verbose $apk |
        Tee-Object -FilePath (Join-Path $artifactRoot 'signature-verification.txt')
    if ($LASTEXITCODE -ne 0) { throw 'A verificação da assinatura de teste falhou.' }
    $badging = & (Join-Path $buildTools.FullName 'aapt.exe') dump badging $apk
    if ($LASTEXITCODE -ne 0) { throw 'A leitura do manifesto compilado falhou.' }
    $badging | Set-Content -LiteralPath (Join-Path $artifactRoot 'package.txt') -Encoding utf8
    $badging | Select-String -Pattern "^package:|^sdkVersion:|^targetSdkVersion:|^application-label:'|^application-debuggable|^launchable-activity:" | Write-Output
    & (Join-Path $buildTools.FullName 'aapt.exe') dump permissions $apk |
        Tee-Object -FilePath (Join-Path $artifactRoot 'permissions.txt')
    if ($LASTEXITCODE -ne 0) { throw 'A leitura das permissões falhou.' }
    $destination = Join-Path $artifactRoot 'AlunUE-Agua-0.1.0-teste.apk'
    Copy-Item -LiteralPath $apk -Destination $destination -Force
    $digest = (Get-FileHash -LiteralPath $destination -Algorithm SHA256).Hash.ToLowerInvariant()
    Set-Content -LiteralPath ($destination + '.sha256') -Value ($digest + '  ' + [IO.Path]::GetFileName($destination)) -Encoding ascii
    Write-Output "APK de teste: $destination"
    Write-Output "SHA-256: $digest"
} finally { Pop-Location }
