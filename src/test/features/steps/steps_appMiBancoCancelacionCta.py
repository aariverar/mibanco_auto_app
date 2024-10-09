from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appModoDeConfirmacion import APP_MODO_CONFIRMACION
from src.test.pages.pages_appAperturaCta import APP_APERTURA_CUENTA
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appCuenta import APP_CUENTA
from src.test.pages.pages_appCancelarCta import APP_CANCELACION_CUENTA
from src.test.pages.pages_appCancelarCta2 import APP_CANCELACION_CUENTA2
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL

@given('Usuario se encuentra logueado en la APP MiBanco cancelacion "{datos}"')
def step_impl(context, datos):
        context.excel="Data.xlsx"
        context.hoja="CancelacionCta"
        context.pageLogin = APP_LOGIN(context)
        context.pageConfirmacion = APP_MODO_CONFIRMACION(context)
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

@when('Usuario selecciona la cuenta a cancelar "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":
        context.pageBase.cerrarBannerDesembolso()
        context.pageBase.seleccionar_Cuenta(datos)

@when('Usuario da tap en el boton de Cancelar Cuenta "{datos}"')
def step_impl(context, datos):
    context.pageCuenta = APP_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageCuenta.click_mas_opciones()
        context.pageCuenta.click_cancelar_cuenta()


@when('Usuario da tap en el boton Si cancelar de la ventana modal "{datos}"')
def step_impl(context, datos):
    context.pageCuenta = APP_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageCuenta.validarModalEstasSeguro()
        context.pageCuenta.click_si_cancelar()

@when('Usuario visualiza la pantalla de confirmacion de cancelacion de cuenta "{datos}"')
def step_impl(context, datos):
    context.pageCancelarCta = APP_CANCELACION_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageCancelarCta.validarConfirmacionCancelacion()
        

@when('Usuario de tap al boton confirmar "{datos}"')
def step_impl(context, datos):
    context.pageCancelarCta = APP_CANCELACION_CUENTA(context)
    if context.ejecutar=="SI":
        context.pageCancelarCta.click_confirmar()
   

@then('Usuario valida la costancia de cancelacion de cuenta "{datos}"')
def step_impl(context, datos):
    context.pageCancelarCta2 = APP_CANCELACION_CUENTA2(context)
    context.pageBase = BASE_PAGE(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":
        context.pageCancelarCta2.validarConstanciaCancelacionCuenta()
        context.pageCancelarCta2.click_btn_ir_inicio()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageMiPerfil.click_quitar()
        context.pageMiPerfil.click_quitar2()

@then('Usuario valida el correo de confirmacion de cancelacion de cuenta "{datos}"')
def step_impl(context, datos):
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.seleccionarCorreoCancelacion()
        context.pageOUTLOOK.cerrarDriver()
