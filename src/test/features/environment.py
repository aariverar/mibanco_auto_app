import time  
from appium.options.android import UiAutomator2Options
from appium import webdriver
from behave import *
from src.test.library.config_mobile import AppConfig
import configparser
from datetime import datetime
import os
import src.test.library.word_generate as generateWord
from src.test.library.utils import *
from src.test.library.variables import *
from src.test.library.storage_connection import *
from src.test.library.db_connection import *
import urllib3
import requests
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import ssl

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
            elif config_Aplicacion()== "MiBanco":
                app_config['app']='kobiton-store:622989'
                print(app_config['app'])
            context.app=app_config['app']
        context.deviceName = app_config['deviceName']
        context.udid = app_config['udid']
        context.versionAndroid = app_config['platformVersion']

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
    context.newNames = []
    context.hostname=os.environ.get('COMPUTERNAME','')
    context.step_img = []
    
    # Configuración de la conexión a la base de datos
    config = configparser.ConfigParser()
    config.read('mobile.properties')
    context.log = config.get('mobile', 'log')
    log = context.log
    if log.lower()=='true':
        context.table_client = get_table_client()

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

    context.start_time=datetime.now()
    generateWord.start_up_word(scenario.name)
    context.name_scenario = scenario.name
    #Inicializacion conexion a BD
    config = configparser.ConfigParser()
    config.read('database.properties')
    context.flagBD = config.get('Database', 'Ejecutar')
    if context.flagBD.lower() =='true':
        context.conexionBD = connectionBD()
   

def after_scenario(context, scenario):
    if context.flagBD.lower() =='true':
        context.conexionBD.close()
        print("[LOG] Se cierra la conexion a la BD")
    if context.state is not None:
        generateWord.borrar_word()
        scenario.set_status("skipped")
        scenario_NewName = {
            'scenario_name': scenario.name,
            'scenario_new_name': "Escenario Skipeado"
        }
        context.newNames.append(scenario_NewName)
    else:
        generateWord.end_to_word(scenario.status.name)
        if hasattr(context, 'nameEscenario'):
            scenario_NewName = {
                'scenario_name': scenario.name,
                'scenario_new_name': context.nameEscenario
            }
            context.newNames.append(scenario_NewName)
        generateWord.end_to_word(scenario.status.name)

        log = context.log
        if log.lower()=='true':
            try:
                context.end_time = datetime.now()
                context.timer = context.end_time - context.start_time
                context.estado = str(scenario.status).split('.')[-1].capitalize()
                context.framework = "Web"
                save_to_table(context, scenario)
            except Exception as e:
                print(f"Error al guardar datos del escenario en la base de datos: {e}")
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
        global contador_ejecuciones
        contador_ejecuciones=0

def after_all(context):
    print("Cerrando conexión mobile global...")
    if hasattr(context, 'mdriver'):
        context.mdriver.quit()
    modify_json_behave(context.step_img, json_behave_path, json_new_path,context.newNames)
    
    # Generate the HTML report
    data_json_path= os.path.join(os.getcwd(), "New.pretty.output")
    data = process_data_json(data_json_path)
    total_scenarios, total_steps, scenarios_information= count_total_scenarios_and_steps(data)
    report_folder = create_report_folder(template_folder_path, report_folder_path, source_files, source_directories, source_dir_path, word_path1)
    
    delete_screenshots_folder(source_directories)
    
    generate_html_for_all_features(html_features_template, report_folder, data, total_scenarios, total_steps, scenarios_information)
    generate_html_for_each_feature(html_for_each_feature_template, report_folder, data)
    json_to_junit('json.pretty.output', 'output.xml')
    
    # Borrar la carpeta de evidencias
    if os.path.exists(word_path1):
        shutil.rmtree(word_path1)
        print(f"La carpeta '{word_path1}' ha sido borrada.")
    else:
        print(f"La carpeta '{word_path1}' no existe.")

def before_step(context, step):
    context.nameImg=[]

def after_step(context, step):
    print(context.state)
    if context.state is None:
        if hasattr(context,"nameImg"):
            step_img={
                'scenario_name': context.name_scenario,
                'step_name': step.name,
                'imagen': context.nameImg
            }
            context.step_img.append(step_img)
    else:
        step_img={
                'scenario_name': context.name_scenario,
                'step_name': step.name,
                'imagen': context.nameImg
            }
        context.step_img.append(step_img)