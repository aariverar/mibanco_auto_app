from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import src.test.library.word_generate as generateWord
from src.test.library.excel_reader import data
import src.test.pages.Objects.excelObjects as excelObjects
from selenium.webdriver.common.by import By
import time
from appium.webdriver.extensions.android.nativekey import AndroidKey
from appium.webdriver.common.appiumby import AppiumBy  # Actualización para MobileBy
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.common.exceptions import WebDriverException
from src.test.library.util_mobile import *

class APP_CANCELACION_CUENTA2:

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
        return data(excelObjects.nombreExcel,excelObjects.nombreAperturaCuenta)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)

    def validarConstanciaCancelacionCuenta(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Tu cuenta ha sido cancelada"]')) 
            )
            generateWord.send_text("Se valida constancia de cancelacion de cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.validarConstanciaCancelacionCuenta()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.validarConstanciaCancelacionCuenta()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.validarConstanciaCancelacionCuenta()")  

    def click_btn_ir_inicio(self):
        try:
            scrollMobile(self.context.mdriver)
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Ir a inicio"]')) 
            )
            btn_incio = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Ir a inicio"]')
            btn_incio.click()
            generateWord.send_text("Se da tap a ir a inicio")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.click_btn_ir_inicio()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.click_btn_ir_inicio()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.click_btn_ir_inicio()")                          
