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

class APP_REGISTRO3:

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
        return data(self.context.excel,self.context.hoja)

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
            input_clave_internet = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="newinternetkeyscreen_newpassword"]')))
            input_clave_internet.click()
            input_clave_internet.send_keys(nueva_clave_internet)
            print(f"[LOG] Se escribe la nueva clave internet {nueva_clave_internet}")
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
            input_clave_internet = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="newinternetkeyscreen_repeatpassword"]')))
            input_clave_internet.click()
            input_clave_internet.send_keys(confirmacion_clave_internet)
            print(f"[LOG] Se escribe la confirmacion de  clave internet {confirmacion_clave_internet}")
            if self.context.mdriver.is_keyboard_shown():
                self.context.mdriver.hide_keyboard()
            generateWord.send_text("Se ingresa confirmacion clave internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ver_tyc(self):
        try:
            text_tyc = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="newinternetkeyscreen_radio_button_accepted_terms_condition"]')
            text_tyc.click()
            generateWord.send_text("Se da tap a TyC")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_acepto_tyc()")

    def acepto_tyc(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary"][2]')) 
            )
            for _ in range(30):
                self.context.mdriver.execute_script("mobile: shell", {
                    'command': 'input', 
                    'args': ['swipe', '500', '1000', '500', '500']  # Ajusta estas coordenadas según el tamaño de tu dispositivo
                })
            btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]')
            generateWord.send_text("Se da tap a TyC")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Aceptar.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_acepto_tyc()")

    def click_crear_nueva_clave_internet(self):
        try:
            time.sleep(2)
            self.context.mdriver.execute_script("mobile: shell", {
                    'command': 'input', 
                    'args': ['swipe', '500', '1000', '500', '500'] 
                    })
            btn_crear_clave = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Crear mi nueva clave de internet"]')
            btn_crear_clave.click()
            generateWord.send_text("Se da tap a crear nueva clave internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_crear_nueva_clave_internet()")

    def validacion_Felicitacion_registro(self):
        try:
            #VALIDACION OBJETO: Felicitaciones
            WebDriverWait(self.context.mdriver, 90).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="¡Felicitaciones!"]')) 
            )
            Log="Exito validacion objeto: Felicitaciones\n"

            #VALIDACION LOGO HAS CREADO TU NUEVA CLAVE DE INTERNET  
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, """//android.widget.TextView[@resource-id="idTextPrimary" and @text="¡Te registraste exitosamente!"]""")))
            Log+="Exito validacion objeto HAS CREADO TU NUEVA CLAVE DE INTERNET \n"
            


            generateWord.send_text("Se valida el banner Felicitaciones!")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. validacion_Felicitacion_registro() \n {Log}")      

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
    
