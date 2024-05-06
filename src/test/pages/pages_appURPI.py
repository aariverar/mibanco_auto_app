from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from src.test.library.util_mobile import UTIL_MOBILE
from selenium.webdriver.support import expected_conditions as EC
import allure
import time


class APP_URPI:

    screenshot_counter = 0
    
    def __init__(self, context):
        self.context = context
        APP_URPI.screenshot_counter += 1

    def abrir_app_URPI(self):
        if self.context is None:
            APP_URPI.screenshot_counter += 1  # Incrementar el contador de capturas
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_abreApp.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        return self.context.mdriver  # Devolver el controlador
    
    def click_permitir(self):
        try:            
            btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
            btn_permitir.click()
            APP_URPI.screenshot_counter += 1  # Incrementar el contador de capturas
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_click_permitir.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            # Si no se encuentra el botón permitir con el ID específico, intenta encontrarlo con otro identificador
            try:
                btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
                btn_permitir.click()
                screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_click_permitir.png"
                UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
                allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")
                self.context.mdriver.close()

    def click_permitirUbicacion(self):
        try:
            btn_permitirUbica = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
            btn_permitirUbica.click()
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_click_permitirUbicacion.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            try:
                btn_permitir = self.context.mdriver.find_element(AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
                btn_permitir.click()
                screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_click_permitirUbicacion.png"
                UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
                allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
            except NoSuchElementException:
                print("No se encontró el elemento necesario para realizar la verificación.")
                self.context.mdriver.close()

    def ingresa_correo_urpi(self, correo):
        try:
            wait = WebDriverWait(self.context.mdriver, 20)
            txt_correo = wait.until(EC.element_to_be_clickable((AppiumBy.CLASS_NAME, "android.widget.EditText")))
            txt_correo.click()
            txt_correo.send_keys(correo)
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_ingresa_correo_urpi.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()

    def click_siguiente(self):
        try:
            btn_siguiente = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Siguiente"]')
            btn_siguiente.click()
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_cilick_siguiente.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()

    def ingresa_password_urpi(self, password):
        try:
            time.sleep(5)
            txt_password = self.context.mdriver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
            txt_password.click()
            txt_password.send_keys(password)
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_ingresa_password_urpi.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()
    
    def click_iniciar(self):
        try:
            btn_iniciar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Iniciar sesión"]')
            btn_iniciar.click()
            time.sleep(5)
            screenshot_name = f"{APP_URPI.screenshot_counter}_screenshot_click_iniciar.png"
            UTIL_MOBILE.capture_screenshot(self.context.mdriver, screenshot_name)
            allure.attach(self.context.mdriver.get_screenshot_as_png(), name=screenshot_name, attachment_type=allure.attachment_type.PNG)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.")
            self.context.mdriver.close()