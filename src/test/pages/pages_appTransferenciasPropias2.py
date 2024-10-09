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
class APP_TRANSFERENCIASPROPIAS2:

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
    
    def verificacion_informacion(self,datos):
        try:
            
            Log="-"
            #VERIFICACION TIPO TRANSFERENCIA
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text, "Entre mis cuentas de Mibanco")]')) 
            )
            Log+="Exito validacion de tipo de transferencia\n"
            
            #VALIDACION CUENTA ORIGEN
            self.context.cuenta_origen=self.get_data()[int(datos)-1][excelObjects.columnCuentaOrigen]
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text,"{self.context.cuenta_origen}")]')) #
            )
            Log+="Exito validacion cuenta origen\n"
            #VALIDACION CUENTA DESTINO
            self.context.cuenta_destino = self.get_data()[int(datos)-1][excelObjects.columnCuentaDestino]
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.cuenta_destino}")]'))
            )
            Log+="Exito validacion cuenta destino\n"

            #VERIFICACION MONTO
       
            monto = self.get_data()[int(datos)-1][excelObjects.columnMonto]
            self.context.monto_formateado = f"{float(monto):.2f}"
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.monto_formateado}")]')) 
            )
            Log+="Exito validacion monto\n"

            generateWord.send_text("Se verifica la informacion de la transferencia")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            scrollMobile(self.context.mdriver)
        except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. validacion_pageModoConfirmacion() \n")     
        except TimeoutException:
            print(f"Error en la verificacion de informacion de la transferencia .verificacion_informacion()\n{Log}")
            generateWord.send_text("Error en la verificacion de informacion de la transferencia")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Error en la verificacion de informacion de la transferencia")
        except Exception as e:
            print(f"No se realizó correctamente el cambio de confirmacion")
            generateWord.send_text(f"Error inesperado {str(e)}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")
        
    def click_terminar(self):
            try:
                scrollMobile(self.context.mdriver)
                scrollMobile(self.context.mdriver)
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Terminar"]')) 
                )
                btn_terminar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Terminar"]')
                btn_terminar.click()
                print("[LOG] Se da tap al boton terminar")
                generateWord.send_text("Se da tap a terminar")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                time.sleep(4)
                
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_terminar()")    