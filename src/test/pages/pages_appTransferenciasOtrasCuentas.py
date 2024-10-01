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
class APP_TRANSFERENCIASOTRASCUENTA:

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
    
    def validacionAotrasCuentasMiBanco(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="A otras cuentas de Mibanco"]')) 
            )
            generateWord.send_text("Se valida el ingreso a Transferencias a otras cuentas de miBanco")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. validacionAotrasCuentasMiBanco()")

    def click_seleccionarUnaCuentaOrigen(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Cuál es la cuenta de origen?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')) 
            )
            selec_cuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Cuál es la cuenta de origen?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')
            text_cuenta = selec_cuenta.get_attribute("text")
            
            if text_cuenta=="Seleccionar una cuenta":       
                selec_cuenta.click()
                return True
            else:
                generateWord.send_text("Cliente solo tiene una cuenta origen")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                return False
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_seleccionarUnaCuentaOrigen()")
    
    def seleccionarCuenta(self, datos):
        cuenta_origen=self.get_data()[int(datos)-1][excelObjects.columnCuentaOrigen]
        max_intentos = 5  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                # Intentar encontrar el elemento
                cuentaSeleccionada = WebDriverWait(self.context.mdriver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{cuenta_origen}"]'))
                )
                # Si se encuentra, realiza la acción deseada
                if cuentaSeleccionada:
                    cuentaSeleccionada.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{cuenta_origen}' encontrado y acción realizada.")
                    generateWord.send_text("Se selecciona cuenta origen")
                    img_name = generateWord.add_image_to_word(self.context.mdriver)
                    self.context.nameImg.append(img_name)
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{cuenta_origen}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1

        if not encontrado:
            print(f"No se pudo encontrar el elemento '{cuenta_origen}' después de {max_intentos} intentos.")
            generateWord.send_text(f"No se pudo encontrar cuenta origen {cuenta_origen}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"No se pudo encontrar cuenta origen '{cuenta_origen}'")

    def ingresar_cuenta_destino(self, datos):
        try:
            cuenta_destino = self.get_data()[int(datos)-1][excelObjects.columnCuentaDestino]
            wait = WebDriverWait(self.context.mdriver, 5)
            input_cuentaDestino = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="toothermibancoaccountss1screen_enterdata_destinationaccount"]')))
            input_cuentaDestino.click()
            input_cuentaDestino.send_keys(cuenta_destino)
            if self.context.mdriver.is_keyboard_shown():
                    self.context.mdriver.hide_keyboard()
            generateWord.send_text("Se ingresa numero de Cuenta Destino")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.ingresar_cuenta_destino()")
    
    def seleccionar_tipo_moneda(self, datos):
            try:
                tipo_moneda = self.get_data()[int(datos)-1][excelObjects.columnTipoMoneda]
                wait = WebDriverWait(self.context.mdriver, 5)
                if tipo_moneda.lower() == "soles":
                    tipoMoneda = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="S/ PEN"]')))
                else:
                    tipoMoneda = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="$ USD"]')))
                tipoMoneda.click()
                generateWord.send_text("Se selecciona tipo de moneda")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                scrollMobile(self.context.mdriver)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresar_monto(self, datos):
            try:
                monto = self.get_data()[int(datos)-1][excelObjects.columnMonto]
                # Verificar si la variable contiene un punto
                if '.' in monto:
                    # Eliminar el punto y convertir a entero multiplicando según la cantidad de decimales
                    parte_entera, parte_decimal = monto.split('.')
    
                    # Verificar la longitud de la parte decimal
                    if len(parte_decimal) == 1:
                        # Si solo hay un dígito decimal, multiplicar por 10
                        monto_convertido = str(int(float(monto) * 100))
                    else:
                        # Si hay más de un dígito, eliminar el punto
                        monto_convertido = monto.replace('.', '')
                else:
                    # Multiplicar por 100 si no contiene punto
                    monto_convertido = str(int(monto) * 100)
                time.sleep(2)
                wait = WebDriverWait(self.context.mdriver, 5)
                input_monto = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="toothermibancoaccountss1screen_enterdata_money_to_transfer"]')))
                input_monto.click()
                input_monto.send_keys(monto_convertido)
                if self.context.mdriver.is_keyboard_shown():
                    self.context.mdriver.hide_keyboard()
                generateWord.send_text("Se ingresa el monto")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    
    def click_siguiente(self):
            try:
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Siguiente"]')) 
                )
                btn_siguiente = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Siguiente"]')
                generateWord.send_text("Se da click a Valida tu identidad con correo electrónico")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                btn_siguiente.click()
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_siguiente()")            
