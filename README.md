## Importante configurar el PATH del sistema con los drivers para que funcione bien el UTIL_WEB

## Para ejecutar los sctripts mediante los features:
`behave --tags=Prueba1`

## Para generar el reporte allure:
`allure generate`

## Para visualizar el reporte: 
`allure open`

## Puedes ejecutar todas las lineas en una sola:
`behave --tags=Prueba1 ; allure generate ; allure open`

## Server http para reporte en cualquier:
`python -m http.server 8000`


## Se agregan mas detalles a allure: 
`behave --tags=Prueba1 ; cp environment.properties allure-results/ ; allure generate ; allure open`

## Generar un archivo de requisitos que incluya todas las dependencias instaladas en tu entorno actual:
`pip freeze > requirements.txt`

## Para instalar todos los Prerequisitos:
`pip install -r requirements.txt` 

## Ejecutar con word:
`behave --tags=Prueba1; python ./src/test/library/generate_word_v2.py`

## Consideraciones de Mobile
Usar la versión de appium v.2.5.2
`npm install -g appium@2.5.2`
Instalar uautomator2:
`npm update -g appium appium-uiautomator2-driver`
Instalar en pip:
`pip install Appium-Python-Client`

## Usar appium Inspector v.2024.3.4

## SDK Tools: https://developer.android.com/studio

## Variables de entorno:
`C:\Android\SDK\cmdline-tools\tools\bin`
`C:\Android\SDK\emulator`
`C:\Android\SDK\platform-tools`

## Comandos (en orden):
`sdkmanager --list`
`sdkmanager "build-tools;30.0.3"`
`sdkmanager "platforms;android-30"`
`sdkmanager "sources;android-30"`
`sdkmanager "system-images;android-30;default;x86_64"`

## Descargar imagenes: 
`sdkmanager "system-images;android-30;default;x86_64"`
## Instalar imagenes:
`avdmanager create avd -n MiDispositivo -k "system-images;android-30;default;x86_64"`
## Ver lista de dispositivos disponibles:
`emulator -list-avds`
## Iniciar emulador :
`emulator -avd MiDispositivo`
## Resetear emulador:
`adb shell reboot`
## Obtener el appPackage y appActiviy:
`C:\SDK\build-tools\30.0.3\aapt.exe dump badging "G:\MI BANCO\APK\Tsoft_Test.apk" | findstr "package: name"`