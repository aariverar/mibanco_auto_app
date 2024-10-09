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

class APP_CUENTA:

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
        return data(self.context.excel,excelObjects.nombreAperturaCuenta)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)


    def click_mas_opciones(self):
        try:
            for _ in range(5):
                scrollMobile(self.context.mdriver)

            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Más opciones"]')) 
            )
            btn_mas_opciones = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Más opciones"]')
            btn_mas_opciones.click()
            generateWord.send_text("Se da tap a mas opciones")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.click_mas_opciones()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.click_mas_opciones()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.click_mas_opciones()")  

    def click_cancelar_cuenta(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Cancelar cuenta"]')) 
            )
            btn_cancelar_cuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Cancelar cuenta"]')
            btn_cancelar_cuenta.click()
            generateWord.send_text("Se da tap a cancelar cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.click_cancelar_cuenta()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.click_cancelar_cuenta()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.click_cancelar_cuenta()")                          

    def validarModalEstasSeguro(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="¿Estás seguro de cancelar esta cuenta?"]')) 
            )
            generateWord.send_text("Se valida modal estas seguro?")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.validarModalEstasSeguro()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.validarModalEstasSeguro()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.validarModalEstasSeguro()")  

    def click_si_cancelar(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Sí, cancelar"]')) 
            )
            btn_cancelar_cuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Sí, cancelar"]')
            btn_cancelar_cuenta.click()
            generateWord.send_text("Se da tap a Si cancelar cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            generateWord.send_text("No se encontró el elemento necesario para realizar la verificación.click_si_cancelar()")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            print("No se encontró el elemento necesario para realizar la verificación.click_si_cancelar()")
            raise AssertionError("ENo se encontró el elemento necesario para realizar la verificación.click_si_cancelar()")   



