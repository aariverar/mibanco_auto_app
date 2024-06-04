
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

    MI_DISPOSITIVO_TEST_LOCAL2 = {
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
        'deviceName':'Galaxy Note10+',
        'platformVersion': '10',
        'udid': 'RF8M822H8YV',
        'app': 'kobiton-store:611646',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true',
        'sessionName': 'Automation Mi Banco',
        'sessionDescription': '',
        'deviceOrientation': 'portrait',
        'captureScreenshots': True,
        'deviceGroup': 'KOBITON',
        'kobi:retainDurationInSeconds': 0,
        'kobiton_server_url': 'https://agalan.mauricio:279c5126-1701-4313-8cb1-1b6429ff4649@api.kobiton.com/wd/hub'
    }

    

