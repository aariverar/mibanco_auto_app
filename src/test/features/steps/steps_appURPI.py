from behave import *
from src.test.pages.pages_appURPI import APP_URPI

# Inicializar el driver de Selenium
pageUrpi = None

@given('ingreso al App URPI "{datos}"')
def step_impl(context, datos):
    context.pageUrpi = APP_URPI(context)
    context.ejecutar =  context.pageUrpi.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageUrpi.abrir_app_URPI()
        context.pageUrpi.inicializarWord(datos)

@when('ingreso mi correo "{datos}"')
def step_impl(context, datos):
    context.pageUrpi = APP_URPI(context)
    if context.ejecutar=="SI":
        context.pageUrpi.click_permitir()
        context.pageUrpi.click_permitirUbicacion()
        context.pageUrpi.ingresa_correo_urpi(datos)
    
@when('doy click en el boton siguiente')
def step_impl(context):
    context.pageUrpi = APP_URPI(context)
    if context.ejecutar=="SI":
        context.pageUrpi.click_siguiente()

@when('ingreso la clave "{datos}"')
def step_impl(context, datos):
    context.pageUrpi = APP_URPI(context)
    if context.ejecutar=="SI":
        context.pageUrpi.ingresa_password_urpi(datos)
    
@then('doy click en el boton ingresar')
def step_impl(context):
    context.pageUrpi = APP_URPI(context)
    if context.ejecutar=="SI":
        context.pageUrpi.click_iniciar()
    else:
        context.state = "NO-EXECUTED"
