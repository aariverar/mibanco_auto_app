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

class BASE_TRANSFERENCIAS:

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
        return data(excelObjects.nombreExcel,self.context.hoja)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        nombre = None
        correo = self.get_data()[int(datos)-1][excelObjects.columnCorreo]
        password = self.get_data()[int(datos)-1][excelObjects.columnPassword]
        generateWord.generate_word_from_table(nombre,correo,password)
    
    def click_transferenciasOtrasCuentasMiBanco(self):
        try:
            WebDriverWait(self.context.mdriver, 90).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="A otras cuentas de Mibanco"]')) 
            )
            btn_transferenciasOtrasCuentasMibanco = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="A otras cuentas de Mibanco"]')
            btn_transferenciasOtrasCuentasMibanco.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_transferenciasOtrasCuentasMiBanco()")
        except TimeoutException:
            print("No aparecion boton omitir tutorial")
    
    def click_transferenciasEntreMisCuentasMiBanco(self):
        try:
            WebDriverWait(self.context.mdriver, 90).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Entre mis cuentas de Mibanco"]')) 
            )
            btn_transferenciasEntreMisCuentasMibanco = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Entre mis cuentas de Mibanco"]')
            btn_transferenciasEntreMisCuentasMibanco.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_transferenciasEntreMisCuentasMiBanco()")
        except TimeoutException:
            print("No aparecion boton omitir tutorial")