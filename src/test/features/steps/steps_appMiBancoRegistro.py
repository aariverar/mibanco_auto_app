from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appOlvideMiClave import APP_OLVIDE
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appOlvideMiClave3 import APP_OLVIDE3
from src.test.pages.pages_appRegistro import APP_REGISTRO
from src.test.pages.pages_appRegistro3 import APP_REGISTRO3

@given('Usuario se encuentra en la APP Mibanco registro "{datos}"')
def step_impl(context, datos):
    context.hoja="Registro"
    context.pageLogin = APP_LOGIN(context)
    context.pageRegistro = APP_REGISTRO(context)
    context.ejecutar =  context.pageRegistro.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageLogin.abrir_appMiBanco()
        context.pageRegistro.inicializarWord(datos)
        context.pageLogin.click_ingresar()
        

@when('Usuario da tap al boton Registrate "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    context.pageRegistro = APP_REGISTRO(context)
    if context.ejecutar=="SI":   
        context.pageLogin.click_registrate_aqui()
        
        

    
@when('Usuario da tap a registrarme con mi tarjeta de debito "{datos}"')
def step_impl(context, datos):
    context.pageRegistro = APP_REGISTRO(context)
    if context.ejecutar=="SI":
        context.pageRegistro.click_registrarme_con_mi_tarjeta_debito()
        context.pageRegistro.validacion_registrate()

@when('Usuario ingresa su documento, tarjeta y clave de cajero registro "{datos}"')
def step_impl(context, datos):
    context.pageRegistro = APP_REGISTRO(context)
    if context.ejecutar=="SI":
        context.pageRegistro.ingresar_nro_doc(datos)
        context.pageRegistro.ingresar_tarjeta(datos)
        context.pageRegistro.ingresar_clave_cajero(datos)
        

@when('Usuario da tap en el boton Siguiente registro "{datos}"')
def step_impl(context, datos):
    context.pageRegistro = APP_REGISTRO(context)
    context.pageOUTLOOK = OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageRegistro.click_siguiente()
        context.pageRegistro.click_valida_identidad_correo()


@when('Usuario extrae el otp del correo registro"{datos}"')
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
        context.pageOUTLOOK.cerrarDriver()

@when('Usuario ingresa el codigo otp y da click en el boton Siguiente "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave2 = APP_OLVIDE2(context)
    context.pageRegistro = APP_REGISTRO(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave2.ingresa_otp_login()
        context.pageRegistro.click_siguiente()


@when('Usuario ingresa la nueva clave de internet registro "{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    if context.ejecutar=="SI":
        context.pageRegistro3.ingresar_nueva_clave_internet(datos)                  

@when('Usuario confirma la nueva clave de internet registro "{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    if context.ejecutar=="SI":
        context.pageRegistro3.ingresar_confirmacion_clave_internet(datos)     

@when('Usuario acepta los terminos y condiciones y da click en el boton Aceptar "{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    if context.ejecutar=="SI":
        context.pageRegistro3.ver_tyc()
        context.pageRegistro3.acepto_tyc()  

@when('Usuario da clik en el boton Crear mi nueva clave de internet registro"{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    if context.ejecutar=="SI":
        context.pageRegistro3.click_crear_nueva_clave_internet()


@then('Usuario valida el mensaje de Felicitaciones te registraste exitosamente "{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    if context.ejecutar=="SI":
        context.pageRegistro3.validacion_Felicitacion_registro()
    else:
        context.state = "NO-EXECUTED"

@then('Usuario valida el correo de confirmacion de registro del cliente en NCD "{datos}"')
def step_impl(context, datos):
    context.pageRegistro3 = APP_REGISTRO3(context)
    context.pageOUTLOOK = OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.click_ultimocorreo()
        context.pageOUTLOOK.validacion_constancia_registro()
        context.pageOUTLOOK.cerrarDriver()
    else:
        context.state = "NO-EXECUTED"
