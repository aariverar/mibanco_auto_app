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
class APP_DESEMBOLSOEAT3:

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
    
    def validacionPage3(self):
        try:
            WebDriverWait(self.context.mdriver, 60).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[contains(@text,"Estás a un paso")]')) 
            )
        except TimeoutException:
            print(f"Error no cargo la page 3")
            generateWord.send_text(f"Error no cargo la page3")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Error no cargo la page3")

    def verifica_informacion_desembolso(self):
        try:
            
            Log="-"
            
            #VALIDACION CUENTA DESTINO
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text,"{self.context.cuenta_a_desembolsar}")]')) #
            )
            Log+="Exito validacion cuenta DESTINO\n"
            #VALIDACION PLAZO
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.cuotas} cuotas")]'))
            )
            Log+="Exito validacion PLAZO\n"

            #VERIFICACION MONTO 
            self.context.monto_formateado = f"S/ {float(self.context.monto_a_desembolsar):,.2f}"
            print(f"Monto formateado: {self.context.monto_formateado}")
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.monto_formateado}")]')) 
            )
            Log+="Exito validacion monto\n"

            #VALIDACION DIA A PAGAR
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.dias} de cada mes")]'))
            )
            Log+="Exito validacion DIA A PAGAR\n"
            generateWord.send_text("Se verifica la informacion del desembolso")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            scrollMobile(self.context.mdriver)
        except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. verifica_informacion_desembolso() \n")     
        except TimeoutException:
            print(f"Error en la verificacion de informacion de la transferencia .verifica_informacion_desembolso()\n{Log}")
            generateWord.send_text(f"Error en la verificacion de informacion del desembolso {Log}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Error en la verificacion de informacion del desembolso")
        except Exception as e:
            print(f"No se realizó correctamente el cambio de confirmacion")
            generateWord.send_text(f"Error inesperado {str(e)}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")
        

    def btn_acepto_TYC(self):
        try:
            scrollMobile(self.context.mdriver)
            btn_acepto_tyc=WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[contains(@text,"Acepto los términos y condiciones de la contratación del préstamo")]')) 
            )
            btn_acepto_tyc.click()
            time.sleep(1)
        except TimeoutException:
            print("No se encontro boton menos informacion")

    def acepto_tyc(self):
        try:
            # WebDriverWait(self.context.mdriver, 30).until(
            #     EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary"][2]')) 
            # )
            for _ in range(30):
                scrollMobile(self.context.mdriver)
            btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]')
            generateWord.send_text("Se da tap a acepto TyC")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Aceptar.click()
            time.sleep(1)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_acepto_tyc()")

    def btn_acepto_TYC_seguro(self):
        try:
            scrollMobile(self.context.mdriver)
            btn_acepto_tyc=WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[contains(@text,"Acepto los términos y condiciones y autorizo el envío del certificado y comunicaciones de mi seguro")]')) 
            )
            btn_acepto_tyc.click()
            time.sleep(1)
        except TimeoutException:
            print("No se encontro boton btn_acepto_TYC_seguro")
    
    def acepto_tyc_seguro(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Términos y condiciones de mi seguro")]')) 
            )
            btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]]')
            display = btn_Aceptar.get_attribute("enabled")
            while (display=="false"):
                btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]]')
                display = btn_Aceptar.get_attribute("enabled")
                scrollMobile(self.context.mdriver)
            

            # for _ in range(30):
            #     scrollMobile(self.context.mdriver)
            #btn_Aceptar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]') #//android.view.View[android.widget.TextView[@resource-id="idTextPrimary" and @text="Acepto"]]
            generateWord.send_text("Se da tap a acepto TyC Seguro")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_Aceptar.click()
            time.sleep(1)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. acepto_tyc_seguro()")


    def boton_desembolsar(self):
        try:
            scrollMobile(self.context.mdriver)
            scrollMobile(self.context.mdriver)
            btn_desembolsar=WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Desembolsar préstamo a mi cuenta"]')) 
            )

            btn_desembolsar.click()
            generateWord.send_text("Se da tap a desembolsar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_acepto_tyc()")

    def esperarPantallaOTP_EAT(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//android.view.View[@resource-id="dynamickeycard_textprimary_newcode"]/preceding-sibling::android.view.View[2]')) 
                    )
        except TimeoutException:
            print(f"Error en la carga de pantalla OTP\n")
            generateWord.send_text("Error en la carga de pantalla OTP")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Error en la carga de pantalla OTP")
        
    def validacion_constancia(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                        EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Hemos depositado tu préstamo en tu cuenta de ahorros."]')) 
                    )
        except TimeoutException:
            print(f"Error en la carga de pantalla constancia\n")
            generateWord.send_text("[Error] No cargío la pantalla constancia")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No cargío la pantalla constancia")
        
    def guardar_numero_operacion(self):
            try:
                scrollMobile(self.context.mdriver)
                WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]')) 
                )
                text_nro_operacion = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Número de operación")]/following-sibling::android.widget.TextView[1]')
                self.context.nrooperacion=text_nro_operacion.get_attribute("text")
                generateWord.send_text(f"El numero de operacion es: {self.context.nrooperacion}")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
                
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.guardar_numero_operacion()") 

    def boton_ver_mis_prestamos(self):
        try:
            scrollMobile(self.context.mdriver)
            scrollMobile(self.context.mdriver)
            scrollMobile(self.context.mdriver)
            btn_ver_prestamos=WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Ver mis préstamos")]')) 
            )

            btn_ver_prestamos.click()
            generateWord.send_text("Se da tap a ver mis prestamos")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. boton_ver_mis_prestamos()")

    
    def validacion_redireccionamiento_ver_prestamos(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Puedes tener hasta 3 préstamos en simultáneo")]')) 
            )
            generateWord.send_text("Se valida redireccionamiento a mis prestamos")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. validacion_redireccionamiento_ver_prestamos()")