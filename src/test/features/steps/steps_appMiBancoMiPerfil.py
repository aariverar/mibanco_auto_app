from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL


@given('Usuario se encuentra logueado en la APP MiBanco MiPerfil "{datos}"')
def step_impl(context, datos):
    context.excel="Data.xlsx"
    context.hoja="MiPerfil"
    context.pageLogin = APP_LOGIN(context)
    context.pageBase = BASE_PAGE(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    context.ejecutar =  context.pageLogin.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageLogin.inicializarWord(datos)
        context.pageLogin.abrir_appMiBanco()
        context.pageLogin.click_ingresar()
        #LOGIN
        context.pageLogin.ingresar_nro_doc(datos)
        context.pageLogin.ingresar_password(datos)
        context.pageLogin.click_ingresar2()
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
        context.pageBase.click_omitir_tutorial()
        context.pageBase.click_Si__ese_es_mi_correo()
        context.pageBase.validacion_Login()

        
@when('Usuario selecciona Opciones')
def step_impl(context):
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":   
        context.pageBase.click_Opciones()

@when('Usuario da tap MiPerfil')
def step_impl(context):
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":   
        context.pageBase.click_MiPerfil()

@then('Usuario valida la pantalla MiPerfil')
def step_impl(context):
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":   
        context.pageMiPerfil.validacion_page_miperfil()

@then('Usuario da tap a Cerrar Sesion "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    context.pageLogin = APP_LOGIN(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":   
        context.pageBase.click_Opciones()
        context.pageBase.click_cerrar_sesion()
        context.pageLogin.click_ingresar()
        #LOGIN
        context.pageLogin.ingresar_nro_doc(datos)
        context.pageLogin.ingresar_password(datos)
        context.pageLogin.click_ingresar2()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageMiPerfil.click_quitar()
        context.pageMiPerfil.click_quitar2()
    else:
        context.state = "NO-EXECUTED"
