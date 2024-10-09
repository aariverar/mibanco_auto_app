from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import src.test.library.word_generate as generateWord
from src.test.library.excel_reader import data
import src.test.pages.Objects.excelObjects as excelObjects
from selenium.webdriver.common.by import By
import allure
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import AppiumBy  # Actualización para MobileBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import WebDriverException

class APP_OLVIDE3:

    screenshot_counter = 0
    digit_map = {
    '0': AndroidKey.DIGIT_0,
    '1': AndroidKey.DIGIT_1,
    '2': AndroidKey.DIGIT_2,
    '3': AndroidKey.DIGIT_3,
    '4': AndroidKey.DIGIT_4,
    '5': AndroidKey.DIGIT_5,
    '6': AndroidKey.DIGIT_6,
    '7': AndroidKey.DIGIT_7,
    '8': AndroidKey.DIGIT_8,
    '9': AndroidKey.DIGIT_9
    }
    def __init__(self, context):
        self.context = context
    
    def get_data(self):
        return data(self.context.excel,excelObjects.nombreOlvide)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)

    def ingresar_nueva_clave_internet(self, datos):
        try:
            nueva_clave_internet = self.get_data()[int(datos)-1][excelObjects.columnClaveInternet]
            wait = WebDriverWait(self.context.mdriver, 30)
            input_clave_internet = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="forgotnewinternetkeyscreen_enterdata_new_password"]')))
            input_clave_internet.click()
            input_clave_internet.send_keys(nueva_clave_internet)
            if self.context.mdriver.is_keyboard_shown():
                self.context.mdriver.hide_keyboard()
            generateWord.send_text("Se ingresa nueva clave internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        
    def ingresar_confirmacion_clave_internet(self, datos):
        try:
            confirmacion_clave_internet = self.get_data()[int(datos)-1][excelObjects.columnNuevaClaveInternet]
            wait = WebDriverWait(self.context.mdriver, 30)
            input_clave_internet = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="forgotnewinternetkeyscreen_enterdata_repeat_new_password"]')))
            input_clave_internet.click()
            input_clave_internet.send_keys(confirmacion_clave_internet)
            if self.context.mdriver.is_keyboard_shown():
                self.context.mdriver.hide_keyboard()
            generateWord.send_text("Se ingresa confirmacion clave internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")


    def click_crear_nueva_clave_internet(self):
        try:
            btn_crear_clave = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Crear mi nueva clave de internet"]')
            btn_crear_clave.click()
            generateWord.send_text("Se da tap a crear nueva clave internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_siguiente()")

    def validacion_Felicitacion_olvide(self):
        try:
            #VALIDACION OBJETO: Felicitaciones
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="¡Felicitaciones!"]')) 
            )
            Log="Exito validacion objeto: Felicitaciones\n"

            #VALIDACION LOGO HAS CREADO TU NUEVA CLAVE DE INTERNET  
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, """//android.widget.TextView[@resource-id="idTextPrimary" and @text="¡Has creado con éxito tu 
 nueva clave de internet!"]""")))
            Log+="Exito validacion objeto HAS CREADO TU NUEVA CLAVE DE INTERNET \n"
            
            #VALIDACION AHORA INGRESA CON TU NUEVA CLAVE
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Ahora ingresa con tu nueva clave"]')) #
            )
            Log+="Exito validacion objeto AHORA INGRESA CON TU NUEVA CLAVE\n"


            generateWord.send_text("Se valida el banne Felicitaciones!")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            Log+="Exito validacion objeto tasa de cambio venta\n"
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. click_Si__ese_es_mi_correo() \n {Log}")      

    def click_ingresar_banca_movil(self):
            try:
                btn_ingresar_banca_movil = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Ingresar a banca móvil"]')
                btn_ingresar_banca_movil.click()
                
                WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="entersinginscreen_enterdata_user"]')) 
                )
            
                generateWord.send_text("Se da tap a ingresar banca movil")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación. click_siguiente()")  
    
