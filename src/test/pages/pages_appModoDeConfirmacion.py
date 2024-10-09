from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
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

class APP_MODO_CONFIRMACION:

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

    def validacion_pageModoConfirmacion(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Elige donde recibir tu código"]')) 
                )
                generateWord.send_text("Se valida ingreso a Page Modo de Confirmación")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)

            except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. validacion_pageModoConfirmacion() \n")      
    
    def tap_opcion_correo(self):
            try:
                btn_opcion_correo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="confirmationmodescreen_radiobuttoncustom_check_email"]')
                btn_opcion_correo.click()
                generateWord.send_text("Se da tap a confirmacion por correo")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación. tap_opcion_correo()")
    
    def tap_validar_otp(self):
            try:
                btn_validar_otp = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Validar"]')
                btn_validar_otp.click()
                generateWord.send_text("Se da tap a Validar")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación. click_siguiente()")


    def validacion_Modo_Confirmacion_Correo(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="confirmationmodescreen_radiobuttoncustom_check_email"]')) 
                )
                btn_opcion_correo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@resource-id="confirmationmodescreen_radiobuttoncustom_check_email"]')
                flagValidacion = btn_opcion_correo.get_attribute("checked")
                print(f"Estado de checked del objeto: {flagValidacion}")
                if(flagValidacion=="true"):
                    generateWord.send_text("Se valida cambio de confirmacion")
                    img_name = generateWord.add_image_to_word(self.context.mdriver)
                    self.context.nameImg.append(img_name)
                else:
                    raise Exception(f"No se realizó correctamente el cambio de confirmacion")
            except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. validacion_pageModoConfirmacion() \n")     
            except TimeoutException:
                print("No se encontró el elemento necesario para realizar la verificación.")
                generateWord.send_text("Encontro el objeto. validacion_Modo_Confirmacion_Correo()")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                raise AssertionError("Encontro el objeto. validacion_Modo_Confirmacion_Correo()")
            except Exception as e:
                print(f"No se realizó correctamente el cambio de confirmacion")
                generateWord.send_text("No se realizó correctamente el cambio de confirmacion")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")
