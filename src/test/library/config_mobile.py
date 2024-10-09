
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


    MI_DISPOSITIVO_MIBANCO_KOBITON = {
        'platformName': 'Android',
        'deviceName':'Galaxy S22',
        'platformVersion': '14',
        'udid': 'RFCW41FCNCL',
        'app': 'kobiton-store:624334',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true',
        'sessionName': 'Automation Mi Banco',
        'sessionDescription': '',
        'deviceOrientation': 'portrait',
        'captureScreenshots': True,
        'deviceGroup': 'KOBITON',
        'kobi:retainDurationInSeconds': 0,
        'kobiton_server_url': 'https://agalan.mauricio:279c5126-1701-4313-8cb1-1b6429ff4649@api.kobiton.com/wd/hub' #https://MiBancoAbraham:0357420e-50f2-4cb2-a2d0-5df7b99da79f@api.kobiton.com/wd/hub
    }

    MI_DISPOSITIVO_HUAWEI_LOCAL2 = {
        'platformName': 'Android',
        'deviceName': 'Huawei',
        'platformVersion': '10',
        'udid': 'UCY6R20716003472',
        'appPackage': 'com.mibanco.bancamovil.qa',
        'appActivity': 'com.mibanco.bancamovil.MainActivity',
        'automationName': 'UiAutomator2',
        'ensureWebviewsHavePages': 'true',
        'nativeWebScreenshot': 'true'
    }
    

