from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appModoDeConfirmacion import APP_MODO_CONFIRMACION
from src.test.pages.pages_appAperturaCta import APP_APERTURA_CUENTA
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2

@given('Usuario se encuentra logueado en la APP MiBanco apertura "{datos}"')
def step_impl(context, datos):
        context.hoja="AperturaCta"
        context.pageLogin = APP_LOGIN(context)
        context.pageConfirmacion = APP_MODO_CONFIRMACION(context)
        context.pageBase = BASE_PAGE(context)
        context.pageOUTLOOK= OUTLOOK_OTP(context)
        context.ejecutar =  context.pageLogin.lecturaexcel(datos)
        if context.ejecutar=="SI":
            context.state = None
            context.pageLogin.abrir_appMiBanco()
            context.pageLogin.inicializarWord(datos)
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

@when('Usuario ingresa a Abre tu cuenta de Ahorros aqui "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.click_abre_tu_cuenta_ahorros()

@when('Usuario selecciona el tipo de cuenta "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.seleccionar_tipo_cuenta(datos)

@when('Usuario selecciona el tipo de moneda "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.seleccionar_tipo_moneda(datos)

@when('Usuario da click en el boton Abrir cuenta del paso 1 "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.click_abrirCuenta()

@when('Usuario da click en el boton Entiendo de la ventana modal "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        flagVal = context.pageAperturaCta.validacionEsteCanal()
        if flagVal=="True":
            context.pageAperturaCta.click_modalEntiendo()
        else:
            context.pageBase.click_Opciones()
            context.pageBase.click_MiPerfil()
            context.pageBase.click_quitar()
            context.pageBase.click_quitar2()
            raise AssertionError("Error, supero el maximo de intentos")

@when('Usuario acepta los terminos y condiciones y residencia fiscal "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.click_check_aceptaTerminosyCondiciones()
        context.pageAperturaCta.click_check_residenciaFiscal()

@when('Usuario da click en el boton Abrir cuenta del paso 2 "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.click_abrirCuenta_verificada()

@when('Usuario extrae codigo de otp desde su correo "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
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
        
@when('Usuario ingresa el codigo otp y da click en el boton Validar 2 "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.ingresa_otp_aperturaCta()
        context.pageAperturaCta.click_Validar()

@then('Usuario valida la constancia de creacion de cuenta exitosa "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageAperturaCta.verificar_creacion_cuenta()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageBase.click_quitar()
        context.pageBase.click_quitar2()

@then('Usuario ingresa a su correo outlook y da click en el ultimo correo recibido apertura "{datos}"')
def step_impl(context, datos):
    context.pageAperturaCta = APP_APERTURA_CUENTA(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()


@then('Usuario valida el correo de confirmacion de apertura de cuenta "{datos}"')
def step_impl(context, datos):
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.seleccionarCorreoConfirmacion()
        context.pageOUTLOOK.validarCorreoConfirmacion()


