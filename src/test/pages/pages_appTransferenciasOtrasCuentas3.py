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
from src.test.library.util_mobile import *
class APP_TRANSFERENCIASOTRASCUENTA3:

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
    
    def verificacion_constancia(self):
        try:
            
            #VERIFICACION BANNER CONSTANCIA
            WebDriverWait(self.context.mdriver, 90).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Constancia de Transferencia"]')) 
            )

        except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. verificacion_constancia() \n")     
        except TimeoutException:
            print(f"Error en la verificacion de informacion de la transferencia .verificacion_constancia()\n")
            generateWord.send_text("Error en la pantalla de constancia")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Error en la pantalla de constancia")
        except Exception as e:
            print(f"No se realizó correctamente el cambio de confirmacion")
            generateWord.send_text(f"Error inesperado {str(e)}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")

    def guardar_numero_operacion(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]')) 
                )
                text_nro_operacion = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]')
                self.context.nrooperacion=text_nro_operacion.get_attribute("text")
                generateWord.send_text(f"El numero de operacion es: {self.context.nrooperacion}")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_transferir()")    
    

