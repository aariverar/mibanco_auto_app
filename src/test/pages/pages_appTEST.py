from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from src.test.library.util_mobile import UTIL_MOBILE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import allure
import time

class APP_TEST:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
        APP_TEST.screenshot_counter += 1

    def abrir_app_TEST(self):
        if self.context is None:
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_abreApp.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        return self.context.mdriver  # Devolver el controlador    

    def click_Registrarse(self):
        try:
            time.sleep(5)
            btnRegistrarse = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Registrarse"]')
            btnRegistrarse.click()
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_click_registrarse.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()
    
    def ingresa_Nombre_Apellido(self, nombreApellido):
        try:
            txtNombreApellido = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Nombre y Apellido"]')
            txtNombreApellido.click()
            txtNombreApellido.send_keys(nombreApellido)
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_ingresa_nombre_apellido.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()

    def ingresa_ID(self, id):
        try:
            txtId = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese ID"]')
            txtId.click()
            txtId.send_keys(id)
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_ingresa_id.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()

    def ingresa_password_1(self, password1):
        try:
            txtPassword1 = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Contraseña"]')
            txtPassword1.click()
            txtPassword1.send_keys(password1)
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_ingresa_pass1.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()
    
    def ingresa_password_2(self, password2):
        try:
            txtPassword2 = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Ingrese Contraseña"]')
            txtPassword2.send_keys(password2)
            self.context.mdriver.press_keycode(4)
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_ingresa_pass2.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()

    def click_Terminos_Condiciones(self):
        try:
            chckTerminos = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.CheckBox[@text="Acepto los términos y condiciones."]')
            chckTerminos.click()
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_click_terminos_condiciones.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()
    
    def click_Registrarse2(self):
        try:
            btnRegistrarse = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Registrarse"]')
            btnRegistrarse.click()
            time.sleep(3)
            screenshot_name = f"{APP_TEST.screenshot_counter}_screenshot_click_registrarse.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()