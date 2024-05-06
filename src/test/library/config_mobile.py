
class AppConfig:

    MI_DISPOSITIVO_URPI_LOCAL = {
        'platformName': 'Android',
        'deviceName': 'MiDispositivo',
        'platformVersion': '11',
        'udid': 'emulator-5554',
        'appPackage': 'com.mibanco.adcurpi',
        'appActivity': 'com.mibanco.adcurpi.mvp.modules.splash.SplashActivity',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true'
    }

    MI_DISPOSITIVO_TEST_LOCAL = {
        'platformName': 'Android',
        'deviceName': 'MiDispositivo',
        'platformVersion': '11',
        'udid': 'emulator-5554',
        'appPackage': 'appinventor.ai_aalexriverar.Tsoft_Test',
        'appActivity': 'appinventor.ai_aalexriverar.Tsoft_Test.Screen1',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true'
    }

    MI_DISPOSITIVO_URPI_KOBITON = {
        'platformName': 'Android',
        'deviceName': 'MiDispositivo',
        'platformVersion': '11',
        'udid': 'RF8NA05R3PM',
        'app': 'kobiton-store:v672276',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true',
        'sessionName': 'Automation Mi Banco',
        'sessionDescription': '',
        'deviceOrientation': 'portrait',
        'captureScreenshots': True,
        'groupId': 2945,  # Group: La Positiva - Pruebas Mobile
        'deviceGroup': 'KOBITON',
        'kobi:retainDurationInSeconds': 0,
        'kobiton_server_url': 'https://luis.mancini:28204dda-b4b7-45f7-be92-ed594f547eaa@api.kobiton.com/wd/hub'
    }