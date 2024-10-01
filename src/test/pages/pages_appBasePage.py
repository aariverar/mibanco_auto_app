from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
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
from src.test.library.util_mobile import *

class BASE_PAGE:

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
        BASE_PAGE.screenshot_counter += 1
    
    def get_data(self):
        return data(excelObjects.nombreExcel,self.context.hoja)

    def lecturaexcel(self, datos):
        ejecucion = self.get_data()[int(datos)-1][excelObjects.columnEjecucion]
        self.context.nameEscenario = f"{self.get_data()[int(datos)-1][excelObjects.columnEscenario]}-{datos}"
        return ejecucion

    def inicializarWord(self, datos):
        nombre = None
        correo = self.get_data()[int(datos)-1][excelObjects.columnCorreo]
        password = self.get_data()[int(datos)-1][excelObjects.columnPassword]
        generateWord.generate_word_from_table(nombre,correo,password)
    
    def click_omitir_tutorial(self):
        try:
            WebDriverWait(self.context.mdriver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Omitir"]')) 
            )
            btn_omitir = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Omitir"]')
            btn_omitir.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. validacionLogin()")
        except TimeoutException:
            print("No aparecion boton omitir tutorial")

    def click_Si__ese_es_mi_correo(self):
        try:
            WebDriverWait(self.context.mdriver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Si, ese es mi correo"]')) 
            )
            btn_si = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Si, ese es mi correo"]')
            btn_si.click()
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Listo"]')) 
            )
            btn_listo = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Listo"]')
            btn_listo.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_Si__ese_es_mi_correo()")
        except TimeoutException:
            print("No aparecion boton si ese es mi correo")


    def validacion_Login(self):
        try:
            #VALIDACION OBJETO: QUE HAGO?
            WebDriverWait(self.context.mdriver, 15).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="que hago"]')) 
            )
            Log="Exito validacion objeto: Que hago?\n"
            #VALIDACION LOGO MIBANCO  
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="logoLogin"]')) 
            )
            Log+="Exito validacion objeto logo MiBanco\n"
            #VALIDACION TASA DE CAMBIO COMPRA
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Compra")]/following-sibling::android.widget.TextView[contains(@text, "US$: S/")][1]')) #
            )
            Log+="Exito validacion objeto tasa de cambio compra\n"
            #VALIDACION TASA DE CAMBIO VENTA
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Venta")]')) #/following-sibling::android.widget.TextView[contains(@text, "US$: S/")][1]
            )
            generateWord.send_text("Se valida el correcto Login")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            Log+="Exito validacion objeto tasa de cambio venta\n"
        except NoSuchElementException:
                print(f"No se encontró el elemento necesario para realizar la verificación. validacion_pageModoConfirmacion() \n")     
        except TimeoutException:
            print("No se encontró el elemento necesario para realizar la verificación.validacion_Login()")
            generateWord.send_text("No realizó correctamente el login")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("Encontro el objeto. validacion_Modo_Confirmacion_Correo()")
        except Exception as e:
            print(f"No se realizó correctamente el cambio de confirmacion")
            generateWord.send_text("No se realizó correctamente el cambio de confirmacion")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError(f"Ocurrió un error inesperado: {str(e)}")

    def click_Opciones(self):
        try:
            WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@content-desc="menu sandwitch"]'))
            )
            btn_menu = self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="menu sandwitch"]')
            btn_menu.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_Opciones()")

    def click_MiPerfil(self):
        try:
            btn_miperfil = WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="menuhamburguer_item_click_my_profile"]')) 
            )
            btn_miperfil.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.click_MiPerfil()")

    def click_quitar(self):
        try:
            generateWord.send_text("Se realiza el desenrolamiento")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_quitar = WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="profilescreen_cardicontextclicktext_text_primary_action_show_unrollingdialog"]')) 
            )
            btn_quitar.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_quitar()")
    
    def click_quitar2(self):
        try:
            time.sleep(1)
            btn_quitar = WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="idTextPrimary" and @text="Quitar"]')) 
            )
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            btn_quitar.click()
            time.sleep(5)
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_quitar2()")


    def click_ModoConfirmacion(self):
        try:
            btn_modoconfirmacion = WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.view.View[@resource-id="menuhamburguer_item_click_confirmation_method"]')) 
            )
            btn_modoconfirmacion.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación.click_ModoConfirmacion()")

    def click_transferencias(self):
        try:
            btn_quitar = WebDriverWait(self.context.mdriver, 30).until(
                EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Transferencias"]')) 
            )
            btn_quitar.click()
        except NoSuchElementException:
            print("No se encontró el elemento necesario para realizar la verificación. click_transferencias()")
    


    def seleccionar_Cuenta(self,datos):
        try:
            for o in range(2):
                cuentas = WebDriverWait(self.context.mdriver, 30).until(
                    EC.presence_of_all_elements_located((AppiumBy.XPATH, '//android.view.View[@resource-id="consultscreen_card_click_select_account"]/android.view.View/android.view.View'))
                )
                print("Se captura Lista de Cuentas")
                numeroDeCuentas=len(cuentas)
                for i in range(numeroDeCuentas):
                    try:
                        print(f"Ingresa al for cuentas {i}")
                        cuenta = cuentas[i]
                        cuenta.click()
                        print("Se da click a la primera cuenta")
                        WebDriverWait(self.context.mdriver, 30).until(
                            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Saldo disponible"]'))
                        )
                        time.sleep(5)
                        numeroCuenta = WebDriverWait(self.context.mdriver, 30).until(
                            EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"N° de cuenta:")]/following-sibling::android.widget.TextView[1]'))
                        )
                        nroCuentaData = self.get_data()[int(datos)-1][excelObjects.columnNroCuenta]
                        textNroCuenta = numeroCuenta.get_attribute("text")
                        if nroCuentaData == textNroCuenta:
                            print("Se valida numero de cuenta")
                            generateWord.send_text("Se selecciona la cuenta a cancelar")
                            img_name = generateWord.add_image_to_word(self.context.mdriver)
                            self.context.nameImg.append(img_name)
                            return "True"
                        else:
                            print("No coincide el numero de cuenta")
                            botonAtras=self.context.mdriver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="icon_back"]')
                            botonAtras.click()
                            btnCerrarDesembolso = WebDriverWait(self.context.mdriver, 10).until(
                                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="cerrar"]')) 
                                )
                            btnCerrarDesembolso.click()
                            cuentas = WebDriverWait(self.context.mdriver, 30).until(
                                EC.presence_of_all_elements_located((AppiumBy.XPATH, '//android.view.View[@resource-id="consultscreen_card_click_select_account"]/android.view.View/android.view.View'))
                            )
                    except StaleElementReferenceException:
                        print(f"Elemento obsoleto en la cuenta {i + 1}, volviendo a intentar")
                        cuentas = WebDriverWait(self.context.mdriver, 30).until(
                            EC.presence_of_all_elements_located((AppiumBy.XPATH, '//android.view.View[@resource-id="consultscreen_card_click_select_account"]/android.view.View/android.view.View'))
                        )
                for p in range(5):
                    scrollMobile(self.context.mdriver)
            print("Error")
            raise Exception("No se encontró la cuenta a cancelar")
       
        except NoSuchElementException:
            print("No se encontro la cuenta a cancelar NoSuchElementException")
            generateWord.send_text("No se encontro la cuenta a cancelar")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
        except Exception as e:
            print(f"No se encontro la cuenta {e}")
            generateWord.send_text("No se encontro la cuenta a cancelar Exception")
            img_name = generateWord.add_image_to_word(self.context.mdriver)
            self.context.nameImg.append(img_name)
            raise AssertionError("No se encontro la cuenta a cancelar")
        

    def cerrarBannerDesembolso(self):
        try:
            btnCerrarDesembolso = WebDriverWait(self.context.mdriver, 5).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="cerrar"]')) 
                )
            btnCerrarDesembolso.click()
        except TimeoutException:
            print("No hay banner de desembolso")