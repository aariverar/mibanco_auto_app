from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appOlvideMiClave import APP_OLVIDE
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appOlvideMiClave3 import APP_OLVIDE3
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL

@given('Usuario se encuentra en la APP MiBanco cambio_clave "{datos}"')
def step_impl(context, datos):
    context.excel="Data.xlsx"
    context.hoja="OlvideMiClave"
    context.pageLogin = APP_LOGIN(context)
    context.pageOlvide = APP_OLVIDE(context)
    context.ejecutar =  context.pageOlvide.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageOlvide.inicializarWord(datos)
        context.pageLogin.abrir_appMiBanco()
        context.pageLogin.click_ingresar()

@when('Usuario da tap en el enlace Olvide mi clave de internet "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    context.pageOlvide = APP_OLVIDE(context)
    if context.ejecutar=="SI":   
        context.pageLogin.click_olvide_mi_clave()
        context.pageOlvide.validacion_olvide_mi_clave()
        

    
@when('Usuario ingresa su documento, tarjeta y clave de cajero "{datos}"')
def step_impl(context, datos):
    context.pageOlvide = APP_OLVIDE(context)
    if context.ejecutar=="SI":
        context.pageOlvide.ingresar_nro_doc(datos)
        context.pageOlvide.ingresar_tarjeta(datos)
        context.pageOlvide.ingresar_clave_cajero(datos)

@when('Usuario da tap en el boton Siguiente cambio_clave "{datos}"')
def step_impl(context, datos):
    context.pageOlvide = APP_OLVIDE(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOlvide.click_siguiente()
        context.pageOlvide.click_valida_identidad_correo()
        

@when('Usuario extrae el otp del correo "{datos}"')
def step_impl(context, datos):
    context.pageOUTLOOK = OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.click_ultimocorreo()
        context.pageOUTLOOK.extraerOTP_Login()
        #context.pageOUTLOOK.cerrarDriver()

@when('Usuario ingresa el codigo otp y da click en el boton Verificar "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    context.pageOlvideClave2 = APP_OLVIDE2(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave2.ingresa_otp_login()
        context.pageLogin.click_siguiente()

@when('Usuario ingresa la nueva clave de internet "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave3 = APP_OLVIDE3(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave3.ingresar_nueva_clave_internet(datos)

@when('Usuario confirma la nueva clave de internet "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave3 = APP_OLVIDE3(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave3.ingresar_confirmacion_clave_internet(datos)                  

@when('Usuario da clik en el boton Crear mi nueva clave de internet "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave3 = APP_OLVIDE3(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave3.click_crear_nueva_clave_internet()
    
@then('Usuario valida el mensaje de Felicitaciones has creado con exito tu clave cambio_clave "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave3 = APP_OLVIDE3(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave3.validacion_Felicitacion_olvide()
        context.pageOlvideClave3.click_ingresar_banca_movil()
    else:
        context.state = "NO-EXECUTED"

@then('Usuario valida el correo de confirmacion de cambio de clave "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave3 = APP_OLVIDE3(context)
    context.pageOUTLOOK = OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.hoja="OlvideMiClave"
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.click_ultimocorreo()
        context.pageOUTLOOK.validacion_constancia_cambio_clave()
        context.pageOUTLOOK.cerrarDriver()
    else:
        context.state = "NO-EXECUTED"
