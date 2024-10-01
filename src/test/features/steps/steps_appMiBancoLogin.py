from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE

@given('Usuario se encuentra en la APP MiBanco "{datos}"')
def step_impl(context, datos):
    context.hoja="Login"
    context.pageLogin = APP_LOGIN(context)
    context.ejecutar =  context.pageLogin.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        
        context.pageLogin.abrir_appMiBanco()
        context.pageLogin.inicializarWord(datos)
        context.pageLogin.click_ingresar()

@when('Usuario ingresa su documento y password "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    if context.ejecutar=="SI":
        
        context.pageLogin.ingresar_nro_doc(datos)
        context.pageLogin.ingresar_password(datos)
    
@when('da click en ingresar "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    if context.ejecutar=="SI":
        context.pageLogin.click_ingresar2()

@when('valida identidad por correo electronico "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.hoja="Login"
        context.pageLogin.click_valida_identidad_correo()
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.click_ultimocorreo()
        context.pageOUTLOOK.extraerOTP_Login()
        context.pageOUTLOOK.cerrarDriver()
        context.pageLogin.ingresa_otp_login()
        context.pageLogin.click_siguiente()
    
@then('Se verifica el login al APP MiBanco correcto "{datos}"')
def step_impl(context, datos):
    context.pageLogin = APP_LOGIN(context)
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":
        context.pageBase.click_omitir_tutorial()
        context.pageBase.click_Si__ese_es_mi_correo()
        context.pageBase.validacion_Login()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageBase.click_quitar()
        context.pageBase.click_quitar2()
    else:
        context.state = "NO-EXECUTED"
