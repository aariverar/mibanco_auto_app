from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import src.test.config.word_generate as generateWord
from src.test.library.excel_reader import data
import src.test.pages.Objects.excelObjects as excelObjects
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import time

class APP_TEST:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
        APP_TEST.screenshot_counter += 1
    
    def get_data(self):
        return data(excelObjects.nombreExcel,excelObjects.nombreTest)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        return ejecucion
    
    def inicializarWord(self, datos):
        nombre = self.get_data()[int(datos)-1][excelObjects.columnNombre]
        correo = None
        password = self.get_data()[int(datos)-1][excelObjects.columnPass1]
        generateWord.generate_word_from_table(nombre,correo,password)

    def abrir_app_TEST(self):
        try:
            # Esperar hasta 20 segundos a que el elemento esté presente
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//android.widget.Button[@text="Registrarse"]')) 
            )
            generateWord.send_text("Se abre la app")
            generateWord.add_image_to_word(self.context.mdriver)
            print("La aplicación se ha abierto correctamente.")
        except Exception as e:
            print("Error al esperar que la aplicación se abra:", e)
            generateWord.send_text("Error al esperar que la aplicación se abra")
            generateWord.add_image_to_word(self.context.mdriver)
            raise AssertionError("Error al esperar que la aplicación se abra")


    def click_Registrarse(self):
        try:
            time.sleep(5)
            btnRegistrarse = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Registrarse"]')
            btnRegistrarse.click()
            generateWord.send_text("Se da Tap a Registrarse")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def ingresa_Nombre_Apellido(self, datos):
        try:
            nombreApellido=self.get_data()[int(datos)-1][excelObjects.columnNombre]
            txtNombreApellido = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Nombre y Apellido"]')
            txtNombreApellido.click()
            txtNombreApellido.send_keys(nombreApellido)
            generateWord.send_text("Se ingresa nombre")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresa_ID(self, datos):
        try:
            Id=self.get_data()[int(datos)-1][excelObjects.columnID]
            txtId = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese ID"]')
            txtId.click()
            txtId.send_keys(Id)
            generateWord.send_text("Se ingresa ID")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def ingresa_password_1(self, datos):
        try:
            password1=self.get_data()[int(datos)-1][excelObjects.columnPass1]
            txtPassword1 = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Contraseña"]')
            txtPassword1.click()
            txtPassword1.send_keys(password1)
            generateWord.send_text("Se ingresa password1")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def ingresa_password_2(self, datos):
        try:
            password2=self.get_data()[int(datos)-1][excelObjects.columnPass2]
            txtPassword2 = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Contraseña"]')
            txtPassword2.send_keys(password2)
            self.context.mdriver.hide_keyboard()
            #self.context.mdriver.press_keycode(4)
            generateWord.send_text("Se ingresa password2")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")

    def click_Terminos_Condiciones(self):
        try:
            chckTerminos = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@text="Acepto los términos y condiciones."]')
            chckTerminos.click()
            generateWord.send_text("Se da Tap a TyC")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
    
    def click_Registrarse2(self):
        try:
            btnRegistrarse = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Registrarse"]')
            btnRegistrarse.click()
            time.sleep(3)
            generateWord.send_text("Se da Tap a registrarse")
            generateWord.add_image_to_word(self.context.mdriver)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")