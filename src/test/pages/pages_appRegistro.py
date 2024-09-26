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

class APP_REGISTRO:

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
        return data(excelObjects.nombreExcel,excelObjects.nombreRegistro)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)


    def click_registrar(self):
        try:
            btn_registrar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Regístrate"]')
            btn_registrar.click()
            generateWord.send_text("Se da click al boton Registrar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_registrarme_con_mi_tarjeta_debito(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, """//android.widget.TextView[@text="Registrarme con 
mi tarjeta de débito"]""")) 
                )
                btn_registrar_con_tarjeta = self.context.mdriver.find_element(AppiumBy.XPATH, """//android.widget.TextView[@text="Registrarme con 
mi tarjeta de débito"]""")
                btn_registrar_con_tarjeta.click()
                generateWord.send_text("Se da click a registrarme con mi tarjeta debito")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_registrarme_con_mi_tarjeta_debito()")            


    def validacion_registrate(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.ScrollView/android.widget.TextView[@resource-id="idTextPrimary"][1]')) 
            )
            generateWord.send_text("Se ingresa a Regístrate")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. validacion_registrate()")
    
    def ingresar_nro_doc(self, datos):
        try:
            nroDoc = self.get_data()[int(datos)-1][excelObjects.columnNroDoc]
            wait = WebDriverWait(self.context.mdriver, 5)
            input_doc = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="registerwithcardscreen_enter_data_doc_number"]')))
            input_doc.click()
            input_doc.send_keys(nroDoc)
            generateWord.send_text("Se ingresa numero de Documento")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        
    def ingresar_tarjeta(self, datos):
            try:
                nroTarjeta = self.get_data()[int(datos)-1][excelObjects.columnNroTarjeta]
                wait = WebDriverWait(self.context.mdriver, 5)
                input_tarjeta = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="registerwithcardscreen_enter_data_doc_number_enter_credit_card"]')))
                input_tarjeta.click()
                input_tarjeta.send_keys(nroTarjeta)
                generateWord.send_text("Se ingresa numero de Tarjeta")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                if self.context.mdriver.is_keyboard_shown():
                    self.context.mdriver.hide_keyboard()
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresar_clave_cajero(self, datos):
            try:
                claveCajero = self.get_data()[int(datos)-1][excelObjects.columnClaveCajero]
                wait = WebDriverWait(self.context.mdriver, 5)
                input_clave_cajero = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="registerwithcardscreen_enter_data_atm_key"]')))
                input_clave_cajero.click()
                input_clave_cajero.send_keys(claveCajero)
                if self.context.mdriver.is_keyboard_shown():
                    self.context.mdriver.hide_keyboard()
                generateWord.send_text("Se ingresar clave Cajero")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    def click_siguiente(self):
        try:
            btn_siguiente = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Siguiente"]')
            btn_siguiente.click()
            generateWord.send_text("Se da click al boton Siguiente")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_siguiente()")

    def click_valida_identidad_correo(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Valida tu identidad con correo electrónico"]')) 
                )
                btn_validar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Valida tu identidad con correo electrónico"]')
                generateWord.send_text("Se da click a Valida tu identidad con correo electrónico")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                btn_validar.click()
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_valida_identidad_correo()")            
