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

@given('Usuario se encuentra logueado en la APP MiBanco transf "{datos}"')
def step_impl(context, datos):
    context.hoja="TransferenciasOtrasCuentas"
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

@given('Usuario ingresa a la opcion de Transferencias y da tap en A otras cuentas de Mibanco "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    context.pageBaseTransf = BASE_TRANSFERENCIAS(context)
    if context.ejecutar=="SI":
        context.state = None
        context.pageBase.click_transferencias()
        context.pageBaseTransf.click_transferenciasOtrasCuentasMiBanco()
        
@when('Usuario selecciona la cuenta origen transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)

    if context.ejecutar=="SI":   
        context.pageTransferencias.validacionAotrasCuentasMiBanco()
        context.pageTransferencias.click_seleccionarUnaCuentaOrigen()
        context.pageTransferencias.seleccionarCuenta(datos)

@when('Usuario ingresa la cuenta destino transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.ingresar_cuenta_destino(datos)

@when('Usuario selecciona el tipo de moneda transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.seleccionar_tipo_moneda(datos)

@when('Usuario ingresa el monto a transferir "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.ingresar_monto(datos)

@when('Usuario da tap en el boton Siguiente transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.click_siguiente()

@when('Usuario verifica informacion de la transferencia "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    if context.ejecutar=="SI":
        context.pageTransferencias2.verificacion_informacion(datos)
        context.pageTransferencias2.click_transferir()
        context.pageTransferencias2.esperarPantallaOTP_Transf()


@when('Usuario ingresa el codigo otp y da click en el boton Validar transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave2 = APP_OLVIDE2(context)
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave2.ingresa_otp_login()
        context.pageTransferencias2.click_validar()


@then('Usuario valida la constancia de transferencia exitosa transferencias_otras_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    context.pageTransferencias3 = APP_TRANSFERENCIASOTRASCUENTA3(context)
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":
        context.pageTransferencias3.verificacion_constancia()
        context.pageTransferencias2.verificacion_informacion(datos)
        context.pageTransferencias3.guardar_numero_operacion()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageBase.click_quitar()
        context.pageBase.click_quitar2()
    else:
        context.state = "NO-EXECUTED"
