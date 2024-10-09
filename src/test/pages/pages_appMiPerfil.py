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

class APP_MIPERFIL:

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
    
    def validacion_page_miperfil(self):
            try:
                #Validacion objeto Dudas o Consultas
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="¿Dudas o consultas?"]')) 
                )

                #Validacion comunicate con nostros
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Comunícate con nosotros al (01) 319-9999"]')) 
                )
                
                #Validacion de nombre ofuscado
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"*** ")][1]')) 
                )
                generateWord.send_text("Se valida ingreso a correcto a MiPerfil")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except TimeoutException:
                generateWord.send_text("Error al ingresar a MiPerfil")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                raise AssertionError("Error al ingresar a mi Perfil")
            except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. validacion_pageModoConfirmacion() \n")      
    
    def click_quitar(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"***@")][1]')) 
                )
                
                btn_quitar = WebDriverWait(self.context.mdriver, 30).until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="profilescreen_cardicontextclicktext_text_primary_action_show_unrollingdialog"]')) 
                )
                generateWord.send_text("Se realiza el desenrolamiento")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                btn_quitar.click()
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación. click_quitar()")
            except Exception as e:
                print(f"[LOG] ERROR CON EL DESENROLAMIENTO {e}")

    def click_quitar2(self):
        try:
            time.sleep(1)
            btn_quitar = WebDriverWait(self.context.mdriver, 30).until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Quitar"]')) )
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_quitar.click()
            time.sleep(5)
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_quitar2()")
        except Exception as e:
                print(f"[LOG] ERROR CON EL DESENROLAMIENTO {e}")
