from behave import *
from src.test.pages.pages_appTEST import APP_TEST


pageTEST = None

@given('usuario ingresa a la app TEST "{datos}"')
def step_impl(context, datos):
    context.pageTEST = APP_TEST(context)
    context.ejecutar =  context.pageTEST.lecturaexcel(datos)
    if context.ejecutar=="SI":
        context.state = None
        context.pageTEST.abrir_app_TEST()
        context.pageTEST.inicializarWord(datos)



@given('usuario da click en boton Registrarse')
def step_impl(context):
    context.pageTEST = APP_TEST(context)
    if context.ejecutar=="SI":
        context.pageTEST.click_Registrarse()

@given('usuario ingresa datos de formulario "{datos}"')
def step_impl(context, datos):
    context.pageTEST = APP_TEST(context)
    if context.ejecutar=="SI":
        context.pageTEST.ingresa_Nombre_Apellido(datos)
        context.pageTEST.ingresa_ID(datos)
        context.pageTEST.ingresa_password_1(datos)
        context.pageTEST.ingresa_password_2(datos)
        context.pageTEST.click_Terminos_Condiciones()

@given('usuario se Registra')
def step_impl(context):
    context.pageTEST = APP_TEST(context)
    if context.ejecutar=="SI":
        context.pageTEST.click_Registrarse2()

@then('se verifica el registro')
def step_impl(context):
    if context.ejecutar=="SI":
        print("valida")
    else:
        context.state = "NO-EXECUTED"