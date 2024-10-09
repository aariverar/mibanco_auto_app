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
from src.test.pages.pages_appTransferenciasPropias import APP_TRANSFERENCIASPROPIAS
from src.test.pages.pages_appTransferenciasPropias2 import APP_TRANSFERENCIASPROPIAS2
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL

@given('Usuario se encuentra logueado en la APP MiBanco transfPropias "{datos}"')
def step_impl(context, datos):
    context.excel="Data.xlsx"
    context.hoja="TransferenciaEntreMisCuentas"
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
        context.pageLogin.esperar_casillas_otp_login()
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

@given('Usuario ingresa a la opcion de Transferencias y da tap a Entre mis cuentas Mibanco "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    context.pageBaseTransf = BASE_TRANSFERENCIAS(context)
    if context.ejecutar=="SI":
        context.state = None
        context.pageBase.click_transferencias()
        context.pageBaseTransf.click_transferenciasEntreMisCuentasMiBanco()
        
@when('Usuario selecciona la cuenta origen entre_mis_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    context.pageTransferenciasPropias = APP_TRANSFERENCIASPROPIAS(context)
    if context.ejecutar=="SI":   
        context.pageTransferenciasPropias.validacionEntreMisCuentasMiBanco()
        context.pageTransferenciasPropias.click_seleccionarUnaCuentaOrigen()
        context.pageTransferenciasPropias.seleccionarCuentaOrigen(datos)

@when('Usuario selecciona la cuenta destino entre_mis_cuentas "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    context.pageTransferenciasPropias = APP_TRANSFERENCIASPROPIAS(context)
    if context.ejecutar=="SI":
        context.pageTransferenciasPropias.click_seleccionarUnaCuentaDestino()
        context.pageTransferenciasPropias.seleccionarCuentaDestino(datos)

@when('Usuario ingresa el monto a transferir transfPropias "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    context.pageTransferenciasPropias = APP_TRANSFERENCIASPROPIAS(context)
    if context.ejecutar=="SI":
        context.pageTransferenciasPropias.ingresar_monto(datos)

@when('Usuario da tap en el boton Siguiente transfPropias "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias = APP_TRANSFERENCIASOTRASCUENTA(context)
    if context.ejecutar=="SI":
        context.pageTransferencias.click_siguiente()

@when('Usuario verifica informacion de la transferencia Propia "{datos}"')
def step_impl(context, datos):
    context.pageTransferenciasPropias2 = APP_TRANSFERENCIASPROPIAS2(context)
    if context.ejecutar=="SI":
        context.pageTransferenciasPropias2.verificacion_informacion(datos)

@when('Usuario da click en el boton transferir "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    if context.ejecutar=="SI":
        context.pageTransferencias2.click_transferir()


@then('Usuario valida la constancia de transferencia exitosa transfPropias "{datos}"')
def step_impl(context, datos):
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    context.pageTransferencias3 = APP_TRANSFERENCIASOTRASCUENTA3(context)
    context.pageBase = BASE_PAGE(context)
    context.pageTransferenciasPropias2 = APP_TRANSFERENCIASPROPIAS2(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":
        context.pageTransferenciasPropias2.verificacion_informacion(datos)
        context.pageTransferencias3.guardar_numero_operacion()
        context.pageTransferenciasPropias2.click_terminar()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageMiPerfil.click_quitar()
        context.pageMiPerfil.click_quitar2()
    else:
        context.state = "NO-EXECUTED"

@then('Usuario valida constancia de transferencia entre mis cuentas en el correo "{datos}"')
def step_impl(context, datos):
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.click_correo_transferencia()
        context.pageOUTLOOK.validacion_constancia_transferencia_propias()
        context.pageOUTLOOK.cerrarDriver()
