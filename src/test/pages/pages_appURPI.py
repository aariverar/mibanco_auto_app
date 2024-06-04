from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import src.test.config.word_generate as generateWord
from src.test.library.excel_reader import data
import src.test.pages.Objects.excelObjects as excelObjects
import allure
import time


class APP_URPI:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
        APP_URPI.screenshot_counter += 1
    
    def get_data(self):
        return data(excelObjects.nombreExcel,excelObjects.nombreUrpi)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        return ejecucion

    def inicializarWord(self, datos):
        nombre = None
        correo = self.get_data()[int(datos)-1][excelObjects.columnCorreo]
        password = self.get_data()[int(datos)-1][excelObjects.columnPassword]
        generateWord.generate_word_from_table(nombre,correo,password)

    def abrir_app_URPI(self):
        if self.context is None:
            generateWord.send_text("Se abre la app")
            generateWord.add_image_to_word(self.context.mdriver)
        return self.context.mdriver  # Devolver el controlador
    
    def click_permitir(self):
        try: 
            time.sleep(10)
            btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
            btn_permitir.click()
            generateWord.send_text("Se da tap a Permitir")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            # Si no se encuentra el botón permitir con el ID específico, intenta encontrarlo con otro identificador
            try:
                btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
                btn_permitir.click()
                generateWord.send_text("Se da tap a Permitir")
                generateWord.add_image_to_word(self.context.mdriver)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    def click_permitirUbicacion(self):
        try:
            btn_permitirUbica = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            btn_permitirUbica.click()
            generateWord.send_text("Se da tap a permitir ubicacion")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            try:
                btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
                btn_permitir.click()
                generateWord.send_text("Se da tap a permitir ubicacion")
                generateWord.add_image_to_word(self.context.mdriver)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresa_correo_urpi(self, datos):
        try:
            correo = self.get_data()[int(datos)-1][excelObjects.columnCorreo]
            wait = WebDriverWait(self.context.mdriver, 20)
            txt_correo = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
            txt_correo.click()
            txt_correo.send_keys(correo)
            generateWord.send_text("Se ingresa correo ")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_siguiente(self):
        try:
            btn_siguiente = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Siguiente"]')
            btn_siguiente.click()
            generateWord.send_text("Se da tap a siguiente")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresa_password_urpi(self, datos):
        try:
            password = self.get_data()[int(datos)-1][excelObjects.columnPassword]
            time.sleep(5)
            txt_password = self.context.mdriver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            txt_password.click()
            txt_password.send_keys(password)
            generateWord.send_text("Se ingresa password ")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def click_iniciar(self):
        try:
            btn_iniciar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Iniciar sesión"]')
            btn_iniciar.click()
            time.sleep(5)
            generateWord.send_text("Se da tap a iniciar")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")