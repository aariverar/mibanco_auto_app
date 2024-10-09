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
class APP_DESEMBOLSOEAT:

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
    
    def validacionPageDesembolsoEAT(self):
        try:
            WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="Desembolsa hasta"]')) 
            )
            generateWord.send_text("Se valida el ingreso a Desembolsar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except TimeoutException:
            generateWord.send_text("[Error] No cargó la page a Desembolsar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No cargó la page a Desembolsar")
        
    def ingresar_monto_a_desembolsar(self, datos):
        try:
            self.context.monto_a_desembolsar = self.get_data()[int(datos)-1][excelObjects.columnMonto]
            wait = WebDriverWait(self.context.mdriver, 5)
            input_monto = wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, '//android.widget.EditText[@resource-id="idEnterDataMoney"]')))
            input_monto.click()
            input_monto.send_keys(self.context.monto_a_desembolsar)
            if self.context.mdriver.is_keyboard_shown():
                    self.context.mdriver.hide_keyboard()
            # generateWord.send_text("Se ingresa monto a Desembolsar")
            # img_name = generateWord.add_image_to_word(self.context.mdriver)
            # self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.ingresar_cuenta_destino()")

    def click_que_dia_pagar(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Qué día quieres pagar?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')) 
            )
            selec_dia_pagar = self.context.mdriver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Qué día quieres pagar?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')
            selec_dia_pagar.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_que_dia_pagar()")
    
    def seleccionar_dia_pagar(self, datos):
        self.context.dias=self.get_data()[int(datos)-1][excelObjects.columnDias]
        max_intentos = 10  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                # Intentar encontrar el elemento
                dia_a_pagar = WebDriverWait(self.context.mdriver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{self.context.dias} de cada mes"]'))
                )
                # Si se encuentra, realiza la acción deseada
                if dia_a_pagar:
                    time.sleep(0.5)
                    dia_a_pagar.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{self.context.dias}' encontrado y acción realizada.")
                    # generateWord.send_text("Se selecciona dia a pagar")
                    # img_name = generateWord.add_image_to_word(self.context.mdriver)
                    # self.context.nameImg.append(img_name)
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{self.context.dias}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1

        if not encontrado:
            print(f"No se pudo encontrar el elemento '{self.context.dias}' después de {max_intentos} intentos.")
            generateWord.send_text(f"[Error] No se pudo encontrar el dia a pagar {self.context.dias}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[Error] No se pudo encontrar el dia a pagar '{self.context.dias}'")

    def click_motivo_prestamo(self):
        try:
            scrollMobile(self.context.mdriver)
            WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_element_located((By.XPATH,'(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Para qué usarás tu préstamo?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')) 
            )
            selec_motivo_prestamo = self.context.mdriver.find_element(AppiumBy.XPATH, '(//android.widget.TextView[@resource-id="idTextPrimary" and @text="¿Para qué usarás tu préstamo?"]/following-sibling::android.view.View/android.widget.TextView[@resource-id="idTextPrimary"])[1]')
            selec_motivo_prestamo.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_motivo_prestamo()")
    
    def seleccionar_motivo_prestamo(self, datos):
        self.context.motivo=self.get_data()[int(datos)-1][excelObjects.columnMotivo]
        max_intentos = 5  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                # Intentar encontrar el elemento
                motivo_prestamo = WebDriverWait(self.context.mdriver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f'(//android.widget.TextView[@text="{self.context.motivo}"]/preceding-sibling::android.widget.CheckBox)[last()]'))
                )
                # Si se encuentra, realiza la acción deseada
                if motivo_prestamo:
                    motivo_prestamo.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{self.context.motivo}' encontrado y acción realizada.")
                    generateWord.send_text("Se selecciona los datos del prestamo")
                    img_name = generateWord.add_image_to_word(self.context.mdriver)
                    self.context.nameImg.append(img_name)
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{self.context.motivo}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1

        if not encontrado:
            print(f"No se pudo encontrar el elemento '{self.context.motivo}' después de {max_intentos} intentos.")
            generateWord.send_text(f"[Error] No se pudo encontrar el motivo del prestamo {self.context.motivo}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[Error] No se pudo encontrar el dia a pagar '{self.context.motivo}'")

    def validacionCuotas(self):
        try:
            scrollMobile(self.context.mdriver)
            scrollMobile(self.context.mdriver)
            WebDriverWait(self.context.mdriver, 45).until(
                    EC.presence_of_element_located((By.XPATH,'//android.widget.TextView[@text="Elige tus cuotas"]')) 
            )
        except TimeoutException:
            generateWord.send_text("[Error] No Cargaron las cuotas correctamente")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No Cargaron las cuotas correctamente")

    def seleccionar_cuotas(self, datos):
        self.context.cuotas=self.get_data()[int(datos)-1][excelObjects.columnCuotas]
        max_intentos = 5  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                scrollMobile(self.context.mdriver)
                # Intentar encontrar el elemento
                cuotas = WebDriverWait(self.context.mdriver, 3).until(
                    EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[@text="{self.context.cuotas} Cuotas"]'))
                )
                # Si se encuentra, realiza la acción deseada
                if cuotas:
                    cuotas.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{cuotas}' encontrado y acción realizada.")
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{cuotas}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1
        if not encontrado:
            print(f"No se pudo encontrar el elemento '{self.context.cuotas}' después de {max_intentos} intentos.")
            generateWord.send_text(f"[Error] No se pudo encontrar la cuota esparada {self.context.cuotas}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[Error] No se pudo encontrar la cuota esparada '{self.context.cuotass}'")

    def click_lo_quiero(self):
        max_intentos = 8  # Número máximo de intentos para evitar un bucle infinito
        intentos = 0
        encontrado = False

        while not encontrado and intentos < max_intentos:
            try:
                scrollMobile(self.context.mdriver)
                scrollMobile(self.context.mdriver)
                # Intentar encontrar el elemento
                lo_quiero = WebDriverWait(self.context.mdriver, 3).until(
                    EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="¡Lo quiero!"]'))
                )
                # Si se encuentra, realiza la acción deseada
                if lo_quiero:
                    generateWord.send_text("Se da tap al boton ¡Lo Quiero!")
                    img_name = generateWord.add_image_to_word(self.context.mdriver)
                    self.context.nameImg.append(img_name)
                    lo_quiero.click()  # Cambia esta línea por la acción que desees realizar
                    encontrado = True
                    intentos=10
                    print(f"Elemento '{lo_quiero}' encontrado y acción realizada.")
            except TimeoutException:
                # Si no encuentra el elemento, realiza el scroll
                print(f"Elemento '{lo_quiero}' no encontrado. Realizando scroll para buscar nuevamente.")
                scrollMobile(self.context.mdriver)  # Asegúrate de tener implementada esta función
                intentos += 1
        if not encontrado:
            print(f"No se pudo encontrar el elemento '{lo_quiero}' después de {max_intentos} intentos.")
            generateWord.send_text(f"[Error] No se pudo encontrar boton lo quiero! {lo_quiero}")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"[Error] No se pudo encontrar boton lo quiero! '{lo_quiero}'")
        

    def modal_por_ahora_no(self):
        try:
            btn_porahora_no = WebDriverWait(self.context.mdriver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[contains(@text, "Por ahora no")]'))
            )
            btn_porahora_no.click()
        except TimeoutException:
            print("Boton continuar no encontrado")

    def seleccionar_seguro_si_o_no(self,datos):
        try:
            seguro_no = WebDriverWait(self.context.mdriver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//android.view.View[@content-desc="No"]'))
            )
            self.context.opcion_seguro=self.get_data()[int(datos)-1][excelObjects.columnSeguro]
            
            if self.context.opcion_seguro.lower()=="si":
                seguro_no.click()
                generateWord.send_text(f"Se selecciona SI al seguro")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
            else:
                generateWord.send_text(f"Se selecciona NO al seguro")
                img_name = generateWord.add_image_to_word(self.context.mdriver)
                self.context.nameImg.append(img_name)
        except TimeoutException:
            generateWord.send_text("[Error] No Cargaron las cuotas correctamente")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No Cargaron las cuotas correctamente")

    def validacion_Cuotas(self):
        try:
            WebDriverWait(self.context.mdriver, 20).until(
                EC.presence_of_element_located((By.XPATH, f'//android.widget.TextView[contains(@text, "{self.context.cuotas} cuotas")]'))
            )
        except TimeoutException:
            generateWord.send_text("[Error] No coinciden la cuota seleccionada")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("[Error] No coinciden la cuota seleccionada")

    def btn_continuar(self):
        try:
            btn_continuar = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Continuar"]')
            btn_continuar.click()
            if self.context.opcion_seguro.lower()=="no":
                btn_porahora_no = WebDriverWait(self.context.mdriver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//android.widget.TextView[contains(@text, "Por ahora no")]'))
                )
                btn_porahora_no.click()
        except TimeoutException:
            print("Boton continuar no encontrado")