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

class APP_OLVIDE2:

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
        return data(self.context.excel,excelObjects.nombreOlvide)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        #self.context.Escenario = self.get_data()[int(datos)-1][excelObjects.columnEscenario]
        self.context.Precondiciones = self.get_data()[int(datos)-1][excelObjects.columnPrecondiciones]
        self.context.ResultadoEsperado = self.get_data()[int(datos)-1][excelObjects.columnResultadoEsperado]
        generateWord.crear_tabla_inicio(self.context.nameEscenario,self.context.Precondiciones,self.context.ResultadoEsperado,self.context)

    def ingresa_otp_login(self):
        try:
            
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="dynamickeycard_textprimary_newcode"]/preceding-sibling::android.view.View[2]'))
            )
            input_otp = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="dynamickeycard_textprimary_newcode"]/preceding-sibling::android.view.View[2]')
            input_otp.click()
            for char in self.context.otp:
                #input_otp.send_keys(nroDoc)
                time.sleep(1)
                self.context.mdriver.press_keycode(APP_OLVIDE2.digit_map[char])
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

                