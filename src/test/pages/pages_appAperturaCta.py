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

class APP_APERTURA_CUENTA:

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


    def click_abre_tu_cuenta_ahorros(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')) 
            )
            lnk_abreTuCuentaAhorros = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')
            lnk_abreTuCuentaAhorros.click()
            generateWord.send_text("Se ingresa Abre tu cuenta de ahorros")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            try:
                btnCerrarDesembolso = WebDriverWait(self.context.mdriver, 5).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="cerrar"]')) 
                )
                btnCerrarDesembolso.click()
                for _ in range(3):
                    scrollMobile(self.context.mdriver)
                WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')) 
                )
                lnk_abreTuCuentaAhorros = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')
                lnk_abreTuCuentaAhorros.click()
                generateWord.send_text("Se ingresa Abre tu cuenta de ahorros")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                print("No aparecio boton abre tu cuenta de ahorros aqui")
            except TimeoutException:
                for _ in range(3):
                    scrollMobile(self.context.mdriver)
                WebDriverWait(self.context.mdriver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')) 
                )
                lnk_abreTuCuentaAhorros = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abre tu cuenta de Ahorros aquí"]')
                lnk_abreTuCuentaAhorros.click()
                generateWord.send_text("Se ingresa Abre tu cuenta de ahorros")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                print("No aparecio boton abre tu cuenta de ahorros aqui")           

    def seleccionar_tipo_cuenta(self, datos):
        try:
            tipoCuenta = self.get_data()[int(datos)-1][excelObjects.columnTipoCuenta]
            # Definir los XPaths de acuerdo a las opciones
            opc_cta_full_ahorro = '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Cuenta Full Ahorro"]'
            opc_cta_ahorro_negocio = '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Cuenta Ahorro Negocios"]'

            # Validar qué opción seleccionar según el valor en Excel
            if tipoCuenta == 'FULL AHORRO':
                opcCuenta = opc_cta_full_ahorro
            elif tipoCuenta == 'AHORRO NEGOCIOS':
                opcCuenta = opc_cta_ahorro_negocio
            else:
                print("Opción no válida en el Excel")
                return

            # Esperar y hacer clic en el elemento correspondiente
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, opcCuenta))
            )
            elemento = self.context.mdriver.find_element(AppiumBy.XPATH, opcCuenta)
            elemento.click()
            generateWord.send_text("Se selecciona el tipo de cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No apareció el botón dentro del tiempo límite.")
        except Exception as e:
            print(f"Se produjo un error: {e}") 

    def seleccionar_tipo_moneda(self, datos):
        try:
            tipoMoneda = self.get_data()[int(datos)-1][excelObjects.columnTipoMoneda]
            # Definir los XPaths de acuerdo a las opciones
            opc_moneda_soles = '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Soles"]'
            opc_moneda_dolares = '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Dólares"]'

            # Validar qué opción seleccionar según el valor en Excel
            if tipoMoneda == 'SOLES':
                opcMoneda = opc_moneda_soles
            elif tipoMoneda == 'DOLARES':
                opcMoneda = opc_moneda_dolares
            else:
                print("Opción no válida en el Excel")
                return

            # Esperar y hacer clic en el elemento correspondiente
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, opcMoneda))
            )
            elemento = self.context.mdriver.find_element(AppiumBy.XPATH, opcMoneda)
            elemento.click()
            generateWord.send_text("Se selecciona el tipo de moneda")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No apareció el botón dentro del tiempo límite.")
        except Exception as e:
            print(f"Se produjo un error: {e}")

    def click_abrirCuenta(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abrir cuenta"]')) 
            )
            btn_abrirCuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Abrir cuenta"]')
            btn_abrirCuenta.click()
            generateWord.send_text("Se da click en abrir cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton abrir cuenta")
    
    def validacionEsteCanal(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Este canal")]'))
            )
            generateWord.send_text('Se valida mensaje "Este canal.."')
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            return "True"
            
        except TimeoutException:
            generateWord.send_text('Error - No se encontro mensaje "Este canal .."')
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Entiendo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Entiendo"]')
            btn_Entiendo.click()
            return "False"
        
    def click_modalEntiendo(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Entiendo"]')) 
            )
            btn_Entiendo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Entiendo"]')
            btn_Entiendo.click()
            generateWord.send_text("Se da click en el modal Entiendo")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton del modal Entiendo")

    def click_check_aceptaTerminosyCondiciones(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.CheckBox[1]')) 
            )
            chk_terminosCondiciones = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.CheckBox[1]')
            chk_terminosCondiciones.click()
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Términos y condiciones"]')) 
            )
            for _ in range(16):
                self.context.mdriver.execute_script("mobile: shell", {
                    'command': 'input', 
                    'args': ['swipe', '500', '1000', '500', '500']  # Ajusta estas coordenadas según el tamaño de tu dispositivo
                })
            btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Acepto"]')
            generateWord.send_text("Se aceptan terminos y condiciones")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Aceptar.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton del modal Entiendo")
    

    def click_check_residenciaFiscal(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.CheckBox[2]')) 
            )
            chk_residenciaFiscal = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.view.View/android.widget.CheckBox[2]')
            chk_residenciaFiscal.click()
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Declaración de Residencia fiscal"]')) 
            )
            btn_NoTengo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="No tengo"]')
            generateWord.send_text("Declaración de Residencia Fiscal")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_NoTengo.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton del modal Entiendo")

    def click_abrirCuenta_verificada(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Abrir cuenta"]')) 
            )
            btn_Entiendo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Abrir cuenta"]')
            btn_Entiendo.click()
            time.sleep(5)
            generateWord.send_text("Se da click en abrir cuenta")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton abrir cuenta")

    def esperarPantallaOtp(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Icon Right"])[2]/preceding-sibling::android.view.View[3]'))
            )
        except TimeoutException:
            print("No abrio caja de otp")
            generateWord.send_text("No cargo la caja de otp")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("No cargo la caja de otp")
    def ingresa_otp_aperturaCta(self):
        try:
            
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Icon Right"])[2]/preceding-sibling::android.view.View[3]'))
            )
            input_otp = self.context.mdriver.find_element(AppiumBy.XPATH, '(//android.widget.ImageView[@content-desc="Icon Right"])[2]/preceding-sibling::android.view.View[3]')
            input_otp.click()
            for char in self.context.otp:
                #input_otp.send_keys(nroDoc)
                time.sleep(1)
                self.context.mdriver.press_keycode(APP_APERTURA_CUENTA.digit_map[char])
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


    def click_Validar(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="idButtonNext"]')) 
            )
            btn_Entiendo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="idButtonNext"]')
            btn_Entiendo.click()
            generateWord.send_text("Se da click en en el boton Validar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton abrir cuenta")


    def verificar_creacion_cuenta(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="¡Felicidades!"]')) 
            )
            generateWord.send_text("Se verifica la constancia de apertura")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            time.sleep(2)

            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"Número de cuenta")]/following-sibling::android.widget.TextView[1]'))
                )
            text_nrocuenta = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Número de cuenta")]/following-sibling::android.widget.TextView[1]')
            self.context.nroCuentaCreada=text_nrocuenta.get_attribute("text")

            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]'))
                )
            text_nro_operacion = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]')
            self.context.nrooperacion=text_nro_operacion.get_attribute("text")


            generateWord.send_text(f"El numero de operacion es: {self.context.nrooperacion} y el numero de cuenta es:{self.context.nroCuentaCreada} ")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            for _ in range(5):
                scrollMobile(self.context.mdriver)

            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Terminar"]')) 
            )
            generateWord.send_text("Se da click en el boton terminar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Terminar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Terminar"]')
            btn_Terminar.click()

        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
        except TimeoutException:
            print("No aparecio boton abrir cuenta")