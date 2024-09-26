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

class APP_LOGIN:

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
        APP_LOGIN.screenshot_counter += 1
    
    def get_data(self):
        return data(excelObjects.nombreExcel,self.context.hoja)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)

    def abrir_appMiBanco(self):
        WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Ingresar"]')) 
        )
        generateWord.send_text("Se ingresa a la APP")
        img_name = generateWord.add_image_to_word(self.context.mdriver)
        self.context.nameImg.append(img_name)
        #if self.context is None:
            #generateWord.send_text("Se abre la app")
            #generateWord.add_image_to_word(self.context.mdriver)
        #return self.context.mdriver  # Devolver el controlador
    
    def click_ingresar(self):
        try:
            btn_ingresar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Ingresar"]')
            btn_ingresar.click()
            generateWord.send_text("Se da click al boton ingresar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se da tap a siguiente")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresar_nro_doc(self, datos):
        try:
            nroDoc = self.get_data()[int(datos)-1][excelObjects.columnNroDoc]
            wait = WebDriverWait(self.context.mdriver, 5)
            input_doc = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="entersinginscreen_enterdata_user"]')))
            input_doc.click()
            input_doc.send_keys(nroDoc)
            generateWord.send_text("Se ingresa numero de Documento")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se ingresa nroDoc ")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresar_password(self, datos):
        try:
            password = self.get_data()[int(datos)-1][excelObjects.columnPassword]
            wait = WebDriverWait(self.context.mdriver, 5)
            input_pass = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="entersinginscreen_enterdata_password"]')))
            input_pass.click()
            input_pass.send_keys(password)
            generateWord.send_text("Se ingresa password")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se ingresa nroDoc ")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def click_ingresar2(self):
        try:
            btn_ingresar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Ingresar"]')
            btn_ingresar.click()
            generateWord.send_text("Se da click a ingresar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se da tap a siguiente")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_valida_identidad_correo(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Valida tu identidad con correo electrónico"]')) 
            )
            btn_validar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Valida tu identidad con correo electrónico"]')
            generateWord.send_text("Se da click a Valida tu identidad con correo electrónico")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_validar.click()
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresa_otp_login(self):
        try:
            
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="dynamickeycard_textprimary_newcode"]/preceding-sibling::android.view.View[5]'))
            )
            input_otp = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="dynamickeycard_textprimary_newcode"]/preceding-sibling::android.view.View[5]')
            input_otp.click()
            for char in self.context.otp:
                #input_otp.send_keys(nroDoc)
                time.sleep(1)
                self.context.mdriver.press_keycode(APP_LOGIN.digit_map[char])
                print(char)

            generateWord.send_text("Se ingresa el numero de OTP")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            if self.context.mdriver.is_keyboard_shown():
                self.context.mdriver.hide_keyboard()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except WebDriverException as e:
            for char in self.context.otp:
                #input_otp.send_keys(nroDoc)
                time.sleep(1)
                self.context.mdriver.execute_script("mobile: shell", {
                'command': 'input', 
                'args': ['text', f'{char}']
                })
                print(char)
            generateWord.send_text("Se ingresa el numero de OTP")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            if self.context.mdriver.is_keyboard_shown():
                self.context.mdriver.hide_keyboard()
            
    def click_siguiente(self):
        try:
            btn_siguiente = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Siguiente"]')
            btn_siguiente.click()
            generateWord.send_text("Se da click al boton Siguiente")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_siguiente()")

    def click_olvide_mi_clave(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Olvidé mi clave de internet"]'))
            )
            btn_olvide = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Olvidé mi clave de internet"]')
            btn_olvide.click()
            generateWord.send_text("Se da click al boton Olvide Mi Clave de Internet")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se da tap a siguiente")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_olvide_mi_clave()")

    def click_registrate_aqui(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Regístrate aquí"]'))
            )
            btn_olvide = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Regístrate aquí"]')
            btn_olvide.click()
            generateWord.send_text("Se da click al boton Registrate Aqui")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            #generateWord.send_text("Se da tap a siguiente")
            #generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_olvide_mi_clave()")    

