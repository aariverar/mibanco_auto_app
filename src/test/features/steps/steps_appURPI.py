from behave import *
from src.test.pages.pages_appURPI import APP_URPI

# Inicializar el driver de Selenium
pageUrpi = None

@given('ingreso al App URPI')
def step_impl(context):
    global pageUrpi
    context.pageUrpi = APP_URPI(context)
    context.pageUrpi.abrir_app_URPI()

@when('ingreso mi correo "{correo}"')
def step_impl(context, correo):
    global pageUrpi
    context.pageUrpi = APP_URPI(context)
    context.pageUrpi.click_permitir()
    context.pageUrpi.click_permitirUbicacion()
    context.pageUrpi.ingresa_correo_urpi(correo)
    
@when('doy click en el boton siguiente')
def step_impl(context):
    global pageUrpi
    context.pageUrpi = APP_URPI(context)
    context.pageUrpi.click_siguiente()

@when('ingreso la clave "{password}"')
def step_impl(context, password):
    global pageUrpi
    context.pageUrpi = APP_URPI(context)
    context.pageUrpi.ingresa_password_urpi(password)
    
@then('doy click en el boton ingresar')
def step_impl(context):
    global pageUrpi
    context.pageUrpi = APP_URPI(context)
    context.pageUrpi.click_iniciar()
