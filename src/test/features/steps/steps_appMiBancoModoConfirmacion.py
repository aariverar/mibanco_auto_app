from behave import *
from src.test.pages.pages_appLogin import APP_LOGIN
from src.test.pages.pages_outlookOTP import OUTLOOK_OTP
from src.test.pages.pages_appBasePage import BASE_PAGE
from src.test.pages.pages_appOlvideMiClave import APP_OLVIDE
from src.test.pages.pages_appOlvideMiClave2 import APP_OLVIDE2
from src.test.pages.pages_appOlvideMiClave3 import APP_OLVIDE3
from src.test.pages.pages_appRegistro import APP_REGISTRO
from src.test.pages.pages_appRegistro3 import APP_REGISTRO3
from src.test.pages.pages_appModoDeConfirmacion import APP_MODO_CONFIRMACION
from src.test.pages.pages_appMiPerfil import APP_MIPERFIL

@given('Usuario se encuentra logueado en la APP MiBanco "{datos}"')
def step_impl(context, datos):
    context.excel="Data.xlsx"
    context.hoja="ActivarConfirmacion"
    context.pageLogin = APP_LOGIN(context)
    context.pageConfirmacion = APP_MODO_CONFIRMACION(context)
    context.pageBase = BASE_PAGE(context)
    context.pageOUTLOOK= OUTLOOK_OTP(context)
    context.ejecutar =  context.pageConfirmacion.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageConfirmacion.inicializarWord(datos)
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

@given('Usuario ingresa a las Opciones "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)

    if context.ejecutar=="SI":
        context.state = None
        context.pageBase.click_Opciones()
        

@given('Usuario da tap al boton modo de confirmacion "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    if context.ejecutar=="SI":
        context.state = None
        context.pageBase.click_ModoConfirmacion() 

@when('Usuario selecciona el modo de confirmacion por correo "{datos}"')
def step_impl(context, datos):
    context.pageConfirmacion = APP_MODO_CONFIRMACION(context)

    if context.ejecutar=="SI":   
        context.pageConfirmacion.validacion_pageModoConfirmacion()
        context.pageConfirmacion.tap_opcion_correo()
        
        

    
@when('Usuario extrae el otp del correo modoConfirmacion "{datos}"')
def step_impl(context, datos):
    context.pageRegistro = APP_REGISTRO(context)
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

@when('Usuario ingresa el codigo otp y da click en el boton Validar "{datos}"')
def step_impl(context, datos):
    context.pageOlvideClave2 = APP_OLVIDE2(context)
    context.pageConfirmacion = APP_MODO_CONFIRMACION(context)
    if context.ejecutar=="SI":
        context.pageOlvideClave2.ingresa_otp_login()
        context.pageConfirmacion.tap_validar_otp()

@then('Usuario valida la activacion del modo confirmacion por correo "{datos}"')
def step_impl(context, datos):
    context.pageBase = BASE_PAGE(context)
    context.pageConfirmacion = APP_MODO_CONFIRMACION(context)
    context.pageMiPerfil = APP_MIPERFIL(context)
    if context.ejecutar=="SI":
        context.pageConfirmacion.validacion_Modo_Confirmacion_Correo()
        context.pageBase.click_Opciones()
        context.pageBase.click_MiPerfil()
        context.pageMiPerfil.click_quitar()
        context.pageMiPerfil.click_quitar2()
    else:
        context.state = "NO-EXECUTED"
