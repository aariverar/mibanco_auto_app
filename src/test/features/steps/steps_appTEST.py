from behave import *
from src.test.pages.pages_appTEST import APP_TEST


pageTEST = None

@given('usuario ingresa a la app TEST')
def step_impl(context):
    global pageTEST
    context.pageTEST = APP_TEST(context)
    context.pageTEST.abrir_app_TEST()


@given('usuario da click en boton Registrarse')
def step_impl(context):
    global pageTEST
    context.pageTEST = APP_TEST(context)
    context.pageTEST.click_Registrarse()

@given('usuario ingresa datos de formulario "{nombre}", "{id}", "{pass1}", "{pass2}"')
def step_impl(context, nombre, id, pass1, pass2):
    global pageTEST
    context.pageTEST = APP_TEST(context)
    context.pageTEST.ingresa_Nombre_Apellido(nombre)
    context.pageTEST.ingresa_ID(id)
    context.pageTEST.ingresa_password_1(pass1)
    context.pageTEST.ingresa_password_2(pass2)
    context.pageTEST.click_Terminos_Condiciones()

@given('usuario se Registra')
def step_impl(context):
    global pageTEST
    context.pageTEST = APP_TEST(context)
    context.pageTEST.click_Registrarse2()

@then('se verifica el registro')
def step_impl(context):
    global pageTEST
    context.pageTEST = APP_TEST(context)
    print("valida")