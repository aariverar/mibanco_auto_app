from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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
        return data(excelObjects.nombreExcel,self.context.hoja)


    def inicializar_driver_chrome(self):
        try:
            ruta_proyecto = os.getcwd()+"/src/test/resources/drivers/chrome/128.0"
            ruta_proyecto = ruta_proyecto+"/chromedriver.exe"
            chrome_options = Options()
            chrome_options.add_argument("--ignore-certificate-errors")
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