import time  
from appium.options.android import UiAutomator2Options
from appium import webdriver
from behave import *
from src.test.library.config_mobile import AppConfig
import configparser
import src.test.config.word_generate as generateWord
from datetime import datetime
from src.test.library.util_mobile import UTIL_MOBILE
import os

# Definir la cantidad de tiempo de espera adicional en segundos
tiempo_espera_kobiton = 20  # Ajusta según sea necesario
contador_ejecuciones = 0

@fixture
def ini_mobile(context, app_config):
    try:
        if 'kobiton_server_url' not in app_config:
            if config_Aplicacion()== "Test":
                app_config['appPackage']='appinventor.ai_aalexriverar.Tsoft_Test'
                app_config['appActivity']='appinventor.ai_aalexriverar.Tsoft_Test.Screen1'
                print(app_config['appPackage'])
            elif config_Aplicacion()== "Urpi":
                app_config['appPackage']='com.mibanco.adcurpi'
                app_config['appActivity']='com.mibanco.adcurpi.mvp.modules.splash.SplashActivity'
                print(app_config['appPackage'])
            context.app=app_config['appPackage']
        else:
            if config_Aplicacion()== "Test":
                app_config['app']='kobiton-store:611647'
                print(app_config['app'])
            elif config_Aplicacion()== "Urpi":
                app_config['app']='kobiton-store:611646'
                print(app_config['app'])
            context.app=app_config['app']
        context.deviceName = app_config['deviceName']
        context.udid = app_config['udid']
        #Convertir capacidades a opciones de Appium
        capabilities_options = UiAutomator2Options().load_capabilities(app_config)
        # Crear el controlador remoto utilizando las opciones de Appium
        context.mdriver = webdriver.Remote(command_executor=app_config['kobiton_server_url'], options=capabilities_options) if 'kobiton_server_url' in app_config else webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capabilities_options)
        
        yield context.mdriver
    except Exception as e:
        print("Error al inicializar el controlador remoto:", e)
        yield context.mdriver

# Función para leer la configuración del archivo mobile.properties
def config_mobile():
    config = configparser.ConfigParser()
    config.read('mobile.properties')
    return config.get('mobile', 'dispositivo')

def config_Aplicacion():
    config = configparser.ConfigParser()
    config.read('mobile.properties')
    return config.get('mobile', 'aplicacion')

def before_all(context):
    global contador_ejecuciones
    print("Inicializando conexión mobile global... -- AFTER ALL")
    context.hostname=os.environ.get('COMPUTERNAME','')
    dispositivo_seleccionado = config_mobile()

    # Obtener la configuración del dispositivo seleccionado
    if hasattr(AppConfig, dispositivo_seleccionado):
        configuracion_dispositivo = getattr(AppConfig, dispositivo_seleccionado)
        use_fixture(ini_mobile, context, app_config=configuracion_dispositivo)
    else:
        print("El dispositivo especificado en mobile.properties no existe en la clase AppConfig.")


def before_scenario(context, scenario):
    global contador_ejecuciones
    print("Inicializando conexión mobile...")
    print(contador_ejecuciones)
    context.appName = " ".join((context.feature.name).rsplit(' ', 2)[-2:])
    generateWord.start_up_word(scenario.name)
    context.start_time=datetime.now()
    contador_ejecuciones += 1
    if contador_ejecuciones > 1:
            try:
                if 'kobiton_server_url' not in context.mdriver.capabilities:
                    context.mdriver.activate_app(context.mdriver.capabilities['appPackage'])
                    print("La aplicación ha sido reabierta.")
                else:
                    # Lógica para Kobiton Store
                    context.mdriver.activate_app(context.mdriver.capabilities['app'])
                    print("La aplicación ha sido reabierta.")
            except Exception as e:
                print("Error al cerrar y abrir la aplicación:", e)

   

def after_scenario(context, scenario):
    config = configparser.ConfigParser()
    config.read('mobile.properties')
    log = config.get('mobile', 'log')
    if context.state is not None:
        generateWord.borar_word()
        scenario.set_status("skipped")
    else:
        generateWord.end_to_word(scenario.status.name)
        if log.lower()=='true':
            context.end_time=datetime.now()
            context.timer=context.end_time-context.start_time
            context.estado=str(scenario.status)
            scenario_name=scenario.name
            fecha=datetime.now().strftime("%d-%m-%Y")
            hora=datetime.now().strftime("%H:%M:%S")
            framework="Appium-Mobile"
            hostname=context.hostname
            filepath=os.getcwd()+"/src/test/resources/log/log.xlsx"
            row_data=[UTIL_MOBILE.get_next_id(filepath),scenario_name,fecha,hora,context.timer.total_seconds(),context.estado,framework,hostname,context.deviceName,context.udid,context.app]
            UTIL_MOBILE.save_excel_locally(filepath,row_data)
            print("[LOG] Se Guarda ejecucion en log.xlsx")
    try:
        if 'kobiton_server_url' not in context.mdriver.capabilities:
            context.mdriver.terminate_app(context.mdriver.capabilities['appPackage'])
            print("La aplicación ha sido cerrada.")
        else:
            # Lógica para Kobiton Store
            context.mdriver.terminate_app(context.mdriver.capabilities['app'])
            print("La aplicación ha sido cerrada.")
    except Exception as e:
        print("Error al cerrar y abrir la aplicación:", e)

def after_all(context):
    print("Cerrando conexión mobile global...")
    if hasattr(context, 'mdriver'):
        context.mdriver.quit()