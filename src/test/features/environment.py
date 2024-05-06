import time  
from appium.options.android import UiAutomator2Options
from appium import webdriver
from behave import *
from src.test.library.config_mobile import AppConfig
import configparser

# Definir la cantidad de tiempo de espera adicional en segundos
tiempo_espera_kobiton = 10  # Ajusta según sea necesario



@fixture
def ini_mobile(context, app_config):
    try:
        # Convertir capacidades a opciones de Appium
        capabilities_options = UiAutomator2Options().load_capabilities(app_config)
        # Crear el controlador remoto utilizando las opciones de Appium
        context.mdriver = webdriver.Remote(command_executor=app_config['kobiton_server_url'], options=capabilities_options) if 'kobiton_server_url' in app_config else webdriver.Remote(command_executor='http://127.0.0.1:4723', options=capabilities_options)
        
        # Agregar una espera para dar tiempo a Kobiton para que complete la instalación de la aplicación
        if 'kobiton_server_url' in app_config:
            time.sleep(tiempo_espera_kobiton)
            
        yield context.mdriver
    except Exception as e:
        print("Error al inicializar el controlador remoto:", e)
        yield context.mdriver

# Función para leer la configuración del archivo mobile.properties
def config_mobile():
    config = configparser.ConfigParser()
    config.read('mobile.properties')
    return config.get('mobile', 'dispositivo')

def before_scenario(context, scenario):
    print("Inicializando conexión mobile...")
    dispositivo_seleccionado = config_mobile()
    
    # Obtener la configuración del dispositivo seleccionado
    if hasattr(AppConfig, dispositivo_seleccionado):
        configuracion_dispositivo = getattr(AppConfig, dispositivo_seleccionado)
        use_fixture(ini_mobile, context, app_config=configuracion_dispositivo)
    else:
        print("El dispositivo especificado en mobile.properties no existe en la clase AppConfig.")

def after_scenario(context, scenario):
    context.mdriver.quit()
