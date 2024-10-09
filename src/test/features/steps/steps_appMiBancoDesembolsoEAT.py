from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL
from src.test.pages.pages_appDesembolsoEAT import APP_DESEMBOLSOEAT
from src.test.pages.pages_appDesembolsoEAT2 import APP_DESEMBOLSOEAT2
from src.test.pages.pages_appDesembolsoEAT3 import APP_DESEMBOLSOEAT3
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appTransferenciasOtrasCuentas2 import APP_TRANSFERENCIASOTRASCUENTA2

@given('Usuario se encuentra logueado en la APP MiBanco DesembolsoEAT "{datos}"')
def step_impl(context, datos):
    context.excel="Data.xlsx"
    context.hoja="DesembolsoEAT"
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

        
@given('Usuario valida el banner de Desembolso')
def step_impl(context):
    context.pageBase = BASE_PAGE(context)
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageBase.validar_BannerDesembolsoEAT()

@when('Usuario da tap al banner de Desembolso')
def step_impl(context):
    context.pageBase = BASE_PAGE(context)
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageBase.click_banner_desembolsoEAT()

@when('Usuario ingresa el monto a desembolsar "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT.validacionPageDesembolsoEAT()
        context.pageDesembolsoEAT.ingresar_monto_a_desembolsar(datos)

@when('Usuario ingresa el dia que desea pagar "{datos}"')
def step_impl(context, datos):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT.click_que_dia_pagar()
        context.pageDesembolsoEAT.seleccionar_dia_pagar(datos)


@when('Usuario ingresa el motivo del prestamo "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT.click_motivo_prestamo()
        context.pageDesembolsoEAT.seleccionar_motivo_prestamo(datos)

@when('Usuario indica el numero de cuotas "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT.validacionCuotas()
        context.pageDesembolsoEAT.seleccionar_cuotas(datos)

@when('Usuario da tap boton LO QUIERO')
def step_impl(context):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT.click_lo_quiero()

@when('Usuario elige si desea seguro o no "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT = APP_DESEMBOLSOEAT(context)
    if context.ejecutar=="SI":
        #context.pageDesembolsoEAT.modal_por_ahora_no()
        context.pageDesembolsoEAT.seleccionar_seguro_si_o_no(datos)
        context.pageDesembolsoEAT.validacion_Cuotas()
        context.pageDesembolsoEAT.btn_continuar()

@when('Usuario selecciona cuenta a desembolsar "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT2 = APP_DESEMBOLSOEAT2(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT2.boton_más_informacion()
        context.pageDesembolsoEAT2.boton_menos_informacion()
        flag=context.pageDesembolsoEAT2.click_seleccionarCuenta_a_Desembolsar(datos)
        if flag:   
            context.pageDesembolsoEAT2.seleccionarCuentaDesembolsar(datos)

@when('Usuario da tap a boton siguiente y valida informacion del desembolso')
def step_impl(context):
    context.pageDesembolsoEAT2 = APP_DESEMBOLSOEAT2(context)
    context.pageDesembolsoEAT3 = APP_DESEMBOLSOEAT3(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT2.click_boton_siguiente()
        context.pageDesembolsoEAT3.validacionPage3()
        context.pageDesembolsoEAT2.boton_más_informacion()
        context.pageDesembolsoEAT3.verifica_informacion_desembolso()
        context.pageDesembolsoEAT2.boton_menos_informacion()

@when('Usuario acepta TyC DesembolsoEAT')
def step_impl(context):
    context.pageDesembolsoEAT3 = APP_DESEMBOLSOEAT3(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT3.btn_acepto_TYC()
        context.pageDesembolsoEAT3.acepto_tyc()
        print(f"OPCION DE SEGURO: {context.opcion_seguro.lower()}")
        if context.opcion_seguro.lower()=="si":
            context.pageDesembolsoEAT3.btn_acepto_TYC_seguro()
            context.pageDesembolsoEAT3.acepto_tyc_seguro()
        context.pageDesembolsoEAT3.boton_desembolsar()
        context.pageDesembolsoEAT3.esperarPantallaOTP_EAT()

@when('Usuario ingresa el codigo otp y da click en el boton Validar DesembolsoEAT')
def step_impl(context):
    context.pageOlvideClave2 = APP_OLVIDE2(context)
    context.pageTransferencias2 = APP_TRANSFERENCIASOTRASCUENTA2(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave2.ingresa_otp_login()
        context.pageTransferencias2.click_validar()

@then('Usuario valida constancia del desembolso')
def step_impl(context):
    context.pageDesembolsoEAT3 = APP_DESEMBOLSOEAT3(context)
    context.pageDesembolsoEAT2 = APP_DESEMBOLSOEAT2(context)
    context.pageBase = BASE_PAGE(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":   
        context.pageDesembolsoEAT3.validacion_constancia()
        context.pageDesembolsoEAT3.verifica_informacion_desembolso()
        context.pageDesembolsoEAT2.boton_más_informacion()
        context.pageDesembolsoEAT3.guardar_numero_operacion()
        context.pageDesembolsoEAT3.boton_ver_mis_prestamos()
        context.pageDesembolsoEAT3.validacion_redireccionamiento_ver_prestamos()

        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageMiPerfil.click_quitar()
        context.pageMiPerfil.click_quitar2()

@then('Usuario valida constancia en el correo "{datos}"')
def step_impl(context,datos):
    context.pageDesembolsoEAT3 = APP_DESEMBOLSOEAT3(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    if context.ejecutar=="SI":   
        context.pageOUTLOOK.inicializar_driver_chrome()
        context.pageOUTLOOK.abrir_Outlook()
        context.pageOUTLOOK.input_email(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.input_password(datos)
        context.pageOUTLOOK.click_siguiente()
        context.pageOUTLOOK.seleccionarCorreoDesembolso()
        context.pageOUTLOOK.validacion_constancia_desembolso()
        context.pageOUTLOOK.cerrarDriver()
    else:
        context.state = "NO-EXECUTED"

