from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appModoDeConfirmacion import APP_MODO_CONFIRMACION
from src.test.pages.pages_appTransferenciasOtrasCuentas import APP_TRANSFERENCIASOTRASCUENTA
from src.test.pages.pages_appTransferenciasOtrasCuentas2 import APP_TRANSFERENCIASOTRASCUENTA2
from src.test.pages.pages_appTransferenciasOtrasCuentas3 import APP_TRANSFERENCIASOTRASCUENTA3
from src.test.pages.pages_appBaseTransferencias import BASE_TRANSFERENCIAS
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL
from src.test.pages.pages_appTransferenciasPropias2 import APP_TRANSFERENCIASPROPIAS2

@given('Usuario se encuentra logueado en la APP MiBanco transf NHP "{datos}"')
def step_impl(context, datos):
    context.excel="DataNoHappy.xlsx"
    context.hoja="TransferenciasOtrasCuentas"
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
        # context.pageLogin.click_valida_identidad_correo()
        # context.pageLogin.esperar_casillas_otp_login()
        # context.pageOUTLOOK.inicializar_driver_chrome()
        # context.pageOUTLOOK.abrir_Outlook()
        # context.pageOUTLOOK.input_email(datos)
        # context.pageOUTLOOK.click_siguiente()
        # context.pageOUTLOOK.input_password(datos)
        # context.pageOUTLOOK.click_siguiente()
        # context.pageOUTLOOK.click_ultimocorreo()
        # context.pageOUTLOOK.extraerOTP_Login()
        # context.pageOUTLOOK.cerrarDriver()
        # context.pageLogin.ingresa_otp_login()
        # context.pageLogin.click_siguiente()
        context.pageBase.click_omitir_tutorial()
        context.pageBase.click_Si__ese_es_mi_correo()
        context.pageBase.validacion_Login()

        

@when('Usuario ingresa menos del monto minimo a transferir "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.ingresar_monto(datos)

@then('Usuario valida el mensaje de error "el monto debe ser mayor o igual a"')
def step_impl(context):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    context.pageBase = BASE_PAGE(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.validacion_mensaje_error_monto_minimo()
        # context.pageBase.click_Opciones()
        # context.pageBase.click_MiPerfil()
        # context.pageMiPerfil.click_quitar()
        # context.pageMiPerfil.click_quitar2()
    else:
        context.state = "NO-EXECUTED"

@then('Usuario valida el mensaje de error "el monto debe ser menor o igual a"')
def step_impl(context):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    context.pageBase = BASE_PAGE(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.validacion_mensaje_error_monto_maximo()
        # context.pageBase.click_Opciones()
        # context.pageBase.click_MiPerfil()
        # context.pageMiPerfil.click_quitar()
        # context.pageMiPerfil.click_quitar2()
    else:
        context.state = "NO-EXECUTED"