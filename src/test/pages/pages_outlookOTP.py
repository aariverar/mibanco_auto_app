from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import src.test.library.word_generate as generateWord
from src.test.library.excel_reader import data
import src.test.pages.Objects.excelObjects as excelObjects
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ServiceChrome
from selenium import webdriver
import time

class OUTLOOK_OTP:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
        #APP_LOGIN.screenshot_counter += 1
    
    def get_data(self):
        return data(self.context.excel,self.context.hoja)


    def inicializar_driver_chrome(self):
        try:
            ruta_proyecto = os.getcwd()+"/src/test/resources/drivers/chrome/128.0"
            ruta_proyecto = ruta_proyecto+"/chromedriver.exe"
            chrome_options = Options()
            chrome_options.add_argument("--ignore-certificate-errors")
            #chrome_options.add_argument("--headless")
            chrome_service = ServiceChrome(ruta_proyecto)
            self.context.driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        except Exception as e:
                print(f"Error al abrir driver chrome: {e}")

    def abrir_Outlook(self): 
        self.context.driver.get("https://outlook.office.com/mail/")
        self.context.driver.implicitly_wait(10)
        self.context.driver.maximize_window()
        # generateWord.send_text("Se ingresa al correo")
        # img_name = generateWord.add_image_to_word(self.context.driver)
        # self.context.nameImg.append(img_name)
        print("Se abre correctamente la URL: https://outlook.office.com/mail/")

    def refrescar_outlook(self):
        self.context.driver.refresh()
        
    def input_email(self,datos):
        try:
            email = self.get_data()[int(datos)-1][excelObjects.columnCorreo]
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="email"]')) 
            )
            input_email=self.context.driver.find_element(By.XPATH,'//input[@type="email"]')
            input_email.send_keys(email)
            # generateWord.send_text("Se inputa el correo")
            # img_name = generateWord.add_image_to_word(self.context.driver)
            # self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_siguiente(self):
        try:
            time.sleep(2) 
            btnSiguiente = WebDriverWait(self.context.driver,30).until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
            btnSiguiente.click()
            print("Se da click en el botón Siguiente.")
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def input_password(self,datos):
        try:
            password = self.get_data()[int(datos)-1][excelObjects.columnContraOutlook]
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//input[@type="password"]')) 
            )
            input_passwd=self.context.driver.find_element(By.XPATH,'//input[@type="password"]')
            input_passwd.send_keys(password)
            # generateWord.send_text("Se inputa el correo")
            # img_name = generateWord.add_image_to_word(self.context.driver)
            # self.context.nameImg.append(img_name)

        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")



    def click_ultimocorreo(self):
        try:
            #ultimo_correo = self.context.driver.find_element(By.XPATH, '//div[@class="EeHm8"]/div[@tabindex="0"]')
            #ultimo_correo.click()
            lblTituloCorreo= WebDriverWait(self.context.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//span[@title='Mibanco_digital_qa@mibanco.com.pe']")))
            lblTituloCorreo.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_correo_registro(self):
        try:
            #ultimo_correo = self.context.driver.find_element(By.XPATH, '//div[@class="EeHm8"]/div[@tabindex="0"]')
            #ultimo_correo.click()
            lblTituloCorreo= WebDriverWait(self.context.driver,30).until(EC.element_to_be_clickable((By.XPATH, " //span[contains(text(),'te damos la bienvenida a los canales')][1]")))
            lblTituloCorreo.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def click_correo_transferencia(self):
            try:
                #ultimo_correo = self.context.driver.find_element(By.XPATH, '//div[@class="EeHm8"]/div[@tabindex="0"]')
                #ultimo_correo.click()
                lblTituloCorreo= WebDriverWait(self.context.driver,30).until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'¡Listo! Tu transferencia se realizó con éxito')][1]")))
                lblTituloCorreo.click()
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.click_cuenta_cancelacion")

    def extraerOTP_Login(self):
        try:
            #time(5)
            etiquetaOtp = WebDriverWait(self.context.driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='UniqueMessageBody_1']//table[2]/tbody/tr/td/div/p")))
            codigoOtp = etiquetaOtp.text
            self.context.otp = codigoOtp #guardar el valor de otp
            time.sleep(2)
            generateWord.send_text("Se ingresa al correo outlook, se da click en el último correo recibido y se extrae otp: " + codigoOtp)
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            print("Se ingresa al correo outlook, se da click en el último correo recibido y se extrae otp: "+ codigoOtp)  
 
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def cerrarDriver(self):
        try:
            self.context.driver.quit()
        except Exception:
            print("No se encontró el elemento necesario para realizar la verificación.")


    def validacion_constancia_cambio_clave(self):
        try:
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "El cambio de tu contraseña ha sido exitoso!")]')) #
            )
            Log="Exito validacion constancia\n"

            time.sleep(2)
            generateWord.send_text("Se el envio de constancia al correo")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. click_Si__ese_es_mi_correo() \n {Log}")
        except TimeoutException:
            print(f"No Se visualiza el envio de constancia al correo")
            generateWord.send_text(f"NO Se visualiza el envio de constancia al correo")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError("NO Se visualiza el envio de constancia al correo")      

    def validacion_constancia_registro(self):
        try:
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "¡Bienvenido a los canales digitales de Mibanco!")]')) #
            )
            Log="Exito validacion constancia\n"

            time.sleep(2)
            generateWord.send_text("Se visualiza el envio de constancia al correo")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. validacion_constancia_registro() \n {Log}")    
        except TimeoutException:
            print(f"No Se visualiza el envio de constancia al correo")
            generateWord.send_text(f"NO Se visualiza el envio de constancia al correo")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError("NO Se visualiza el envio de constancia al correo")            

    def seleccionarCorreoCancelacion(self):
        try: 
            tiempoTotal = 300
            intervaloRefresh = 10
            finTiempo = time.time() + tiempoTotal
       
            while time.time() < finTiempo:
                try:
                    lblTituloCorreo = WebDriverWait(self.context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'¡Listo! Tu cuenta de ahorros Mibanco se canceló con éxito')][1]")))
                    lblTituloCorreo.click()
                    print("Correo encontrado y clickeado.")
                    WebDriverWait(self.context.driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.nroCuentaData}")]')) 
                    )
                    time.sleep(3)
                    generateWord.send_text(f"Se visualiza constancia de cancelacion de cuenta")
                    img_name = generateWord.add_image_to_word_web(self.context.driver)
                    self.context.nameImg.append(img_name)
                    return
 
                except TimeoutException:
                    self.context.driver.refresh()
                    time.sleep(intervaloRefresh)  
            print("No se encontró el correo en el tiempo especificado.")
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

        
    def seleccionarCorreoConfirmacion(self):
        try: 
            tiempoTotal = 300
            intervaloRefresh = 10
            finTiempo = time.time() + tiempoTotal
       
            while time.time() < finTiempo:
                try:
                    lblTituloCorreo = WebDriverWait(self.context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'¡Felicidades! Tu cuenta de ahorros Mibanco se creó con éxito. Cuenta: {self.context.nroCuentaCreada}')]")))
                    lblTituloCorreo.click()
                    print("Correo encontrado y clickeado.")
                    return
 
                except TimeoutException:
                    self.context.driver.refresh()
                    time.sleep(intervaloRefresh)  
            print("No se encontró el correo en el tiempo especificado.")
 
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def validarCorreoConfirmacion(self):
        textoOutput = ""
        try:
            time.sleep(2)
            numeroConfirmacion = WebDriverWait(self.context.driver, 30).until(EC.presence_of_element_located((By.XPATH, "//table/tbody/tr/td/table[4]/tbody/tr/td/table/tbody/tr/td/table[4]/tbody/tr/td/div/p")))        
            textoOutput = numeroConfirmacion.text.strip()
            textoEsperado = self.context.nrooperacion
            time.sleep(2)
            assert textoOutput == textoEsperado
            generateWord.send_text("Se ingresa al último correo recibido y se verifica el correo de confirmación con el N° de operación: " + textoEsperado)
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except AssertionError:
            print(f"La verificación falló: el texto obtenido no coincide con el texto esperado. Texto obtenido: {textoOutput}")
            generateWord.send_text(f"NO se encontró el correo de confirmación. Texto obtenido: {textoOutput}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"La verificación falló: el texto obtenido no coincide con el texto esperado. Texto obtenido: {textoOutput}")
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. Texto obtenido: {textoOutput}")
            generateWord.send_text(f"NO se encontró el correo de confirmación. Texto obtenido: {textoOutput}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"No se encontró el elemento necesario para realizar la verificación. Texto obtenido: {textoOutput}")
        except TimeoutException:
            print(f"No se encontró el elemento necesario para realizar la verificación. Texto obtenido: {textoOutput}")
            generateWord.send_text(f"NO se encontró el correo de confirmación. Texto obtenido: {textoOutput}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"No se encontró el elemento necesario para realizar la verificación. Texto obtenido: {textoOutput}")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {str(e)}")
            generateWord.send_text(f"Ocurrió un error inesperado: {str(e)}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")        

    def validacion_constancia_transferencia_propias(self):
        try:
            Log="-"
            #VALIDACION DE MONTO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.monto_formateado}")]')) 
            )
            Log="Exito validacion monto\n"
            #VALIDACION TIPO DE TRANSFERENCIA
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "Entre mis cuentas de Mibanco")]')) 
            )
            Log+="Exito validacion tipo transferencia\n"

            #VALIDACION DE NUMERO DE OPERACION
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.nrooperacion}")]')) 
            )
            Log+="Exito validacion numero de operacion\n"
            #VALIDACION DE CUENTA ORIGEN
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuenta_origen}")]')) 
            )
            Log+="Exito validacion cuenta origen\n"
            #VALIDACION DE CUENTA DESTINO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuenta_destino}")]')) 
            )
            Log+="Exito validacion cuenta destino\n"
            #VALIDACION DE CANAL
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "app Mibanco Móvil")]')) 
            )
            Log+="Exito validacion de canal\n"
            time.sleep(2)
            generateWord.send_text("Se el envio de constancia de la transferencia")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. validacion_constancia_transferencia_propias() \n {Log}")
        except TimeoutException:
            print(f"No Se visualiza el envio de constancia al correo")
            generateWord.send_text(f"[ERROR] Error al validar el correo de la operacion {Log}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[ERROR] Error al validar el correo de la operacion {Log}")        

    def validacion_constancia_transferencia_otras_cuentas(self):
        try:
            Log="-"
            #VALIDACION DE MONTO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.monto_formateado}")]')) 
            )
            Log+="Validacion de monto\n"
            #VALIDACION TIPO DE TRANSFERENCIA
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, '//p[contains(text(), "A otras cuentas de Mibanco")]')) 
            )
            Log+="Validacion de tipo de transferencia\n"

            #VALIDACION DE NUMERO DE OPERACION
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.nrooperacion}")]')) 
            )
            Log+="Validacion de numero de operacion\n"
            #VALIDACION DE CUENTA ORIGEN
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuenta_origen}")]')) 
            )
            Log+="Validacion de cuenta origen\n"
            #VALIDACION DE CUENTA DESTINO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuenta_destino}")]')) 
            )
            Log+="Validacion de cuenta DESTINO\n"
            #VALIDACION DE CANAL
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "app Mibanco Móvil")]')) 
            )
            Log+="Validacion de cuenta canal\n"
            time.sleep(2)
            generateWord.send_text("Se el envio de constancia de la transferencia")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. validacion_constancia_transferencia_otras_cuentas() \n {Log}")
        except TimeoutException:
            print(f"No Se visualiza el envio de constancia al correo")
            generateWord.send_text(f"[ERROR] Error al validar el correo de la operacion {Log}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[ERROR] Error al validar el correo de la operacion {Log}")          
        
    def seleccionarCorreoDesembolso(self):
        try: 
            tiempoTotal = 120
            intervaloRefresh = 10
            finTiempo = time.time() + tiempoTotal
       
            while time.time() < finTiempo:
                try:
                    lblTituloCorreo = WebDriverWait(self.context.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'¡Desembolso exitoso! Tu dinero ya está disponible en tu cuenta. Préstamo: {self.context.nrooperacion}')]")))
                    lblTituloCorreo.click()
                    print("Correo encontrado y clickeado.")
                    time.sleep(1)
                    return
 
                except TimeoutException:
                    self.context.driver.refresh()
                    time.sleep(intervaloRefresh)  
            print("No se encontró el correo en el tiempo especificado.")
        except TimeoutException:
            print(f"No se encontró el correo de desembolso: {self.context.nrooperacion}")
            generateWord.send_text(f"No se encontró el correo de desembolso: {self.context.nrooperacion}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"No se encontró el elemento necesario para realizar la verificación. Texto obtenido: {self.context.nrooperacion}")
        
    def validacion_constancia_desembolso(self):
        try:
            Log="-"
            #VALIDACION DE MONTO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.monto_formateado}")]')) 
            )
            Log+="Validacion de monto\n"

            #VALIDACION TIPO DE PLAZOS
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuotas} cuotas")]')) 
            )
            Log+="Validacion de las cuotas\n"

            #VALIDACION DE NUMERO DE OPERACION
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.nrooperacion}")]')) 
            )
            Log+="Validacion de numero de operacion\n"

            #VALIDACION DE CUENTA DESTINO
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.cuenta_a_desembolsar}")]')) 
            )
            Log+="Validacion de cuenta DESTINO\n"

            #VALIDACION DIA A PAGAR
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "{self.context.dias} de cada mes")]'))
            )
            Log+="Exito validacion DIA A PAGAR\n"

            #VALIDACION DE CANAL
            WebDriverWait(self.context.driver, 30).until(
                EC.presence_of_element_located((By.XPATH, f'//p[contains(text(), "app Mibanco Móvil")]')) 
            )
            Log+="Validacion de cuenta canal\n"

            time.sleep(2)
            generateWord.send_text("Se valida la constancia de desembolso")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print(f"No se encontró el elemento necesario para realizar la verificación. validacion_constancia_desembolso() \n {Log}")
        except TimeoutException:
            print(f"No Se visualiza el envio de constancia al correo")
            generateWord.send_text(f"[ERROR] Error al validar el correo del desembolso {Log}")
            img_name = generateWord.add_image_to_word_web(self.context.driver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[ERROR] Error al validar el correo del desembolso {Log}")          

        