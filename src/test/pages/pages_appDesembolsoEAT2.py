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
class APP_DESEMBOLSOEAT2:

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
    
    def boton_más_informacion(self):
        try:
            btn_mas_informacion=WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="Más información"]')) 
            )
            btn_mas_informacion.click()
            time.sleep(1)
            generateWord.send_text("Se da tap a mas informacion")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except TimeoutException:
            generateWord.send_text("[Error] No se encontró el boton más informacion de la Page 2")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No se encontró el boton más informacion de la Page 2")
        
    def boton_menos_informacion(self):
        try:
            btn_menos_informacion=WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="Menos información"]')) 
            )
            btn_menos_informacion.click()
            time.sleep(1)
        except TimeoutException:
            print("No se encontro boton menos informacion")
        
    def click_seleccionarCuenta_a_Desembolsar(self,datos):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'(//android.widget.TextView[@resource-id="idTextPrimary" and @text="Desembolsar el dinero en"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')) 
            )
            selec_cuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="idTextPrimary" and @text="Desembolsar el dinero en"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')
            text_cuenta = selec_cuenta.get_attribute("text")
            
            if text_cuenta=="Selecciona la cuenta":       
                selec_cuenta.click()
                return True
            else:
                self.context.cuenta_a_desembolsar=text_cuenta
                generateWord.send_text(f"Cliente solo tiene una para desembolsar {self.context.cuenta_a_desembolsar}")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                return False
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_seleccionarCuenta_a_Desembolsar()")

    def seleccionarCuentaDesembolsar(self, datos):
        self.context.cuenta_a_desembolsar=self.get_data()[int(datos)-1][excelObjects.columnCuentaDesembolsar]
        max_intentos = 5  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                # Intentar encontrar el elemento
                cuentaSeleccionada = WebDriverWait(self.context.mdriver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{self.context.cuenta_a_desembolsar}"]'))
                )
                # Si se encuentra, realiza la acción deseada
                if cuentaSeleccionada:
                    cuentaSeleccionada.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{self.context.cuenta_a_desembolsar}' encontrado y acción realizada.")
                    generateWord.send_text("Se selecciona cuenta a desembolsar")
                    img_name = generateWord.add_image_to_word(self.context.mdriver)
                    self.context.nameImg.append(img_name)
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{self.context.cuenta_a_desembolsar}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1

        if not encontrado:
            print(f"No se pudo encontrar el elemento '{self.context.cuenta_a_desembolsar}' después de {max_intentos} intentos.")
            generateWord.send_text(f"No se pudo encontrar cuenta a desembolsar {self.context.cuenta_a_desembolsar}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"No se pudo encontrar cuenta a desembolsar '{self.context.cuenta_a_desembolsar}'")

    def click_boton_siguiente(self):
        try:
            scrollMobile(self.context.mdriver)
            btn_siguiente=WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="Siguiente"]')) 
            )    
            btn_siguiente.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_boton_siguiente()")
    
   