Feature: Flujos Automatizados APP Mi Banco

  @NCD_Login @HP
  Scenario Outline: Login Correcto APP MiBanco
    Given Usuario se encuentra en la APP MiBanco "<datos>"
    When Usuario ingresa su documento y password "<datos>"
    And da click en ingresar "<datos>"
    And valida identidad por correo electronico "<datos>"
    Then Se verifica el login al APP MiBanco correcto "<datos>"

    Examples:
      | datos |
      |     1 |


@NCD_OlvideMiClave @HP
  Scenario Outline: Cambio de clave exitoso en APP MiBanco
    Given Usuario se encuentra en la APP MiBanco cambio_clave "<datos>"
    When Usuario da tap en el enlace Olvide mi clave de internet "<datos>"
    And Usuario ingresa su documento, tarjeta y clave de cajero "<datos>" 
    And Usuario da tap en el boton Siguiente cambio_clave "<datos>"
    And Usuario extrae el otp del correo "<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Verificar "<datos>"
    And Usuario ingresa la nueva clave de internet "<datos>"
    And Usuario confirma la nueva clave de internet "<datos>"
    And Usuario da clik en el boton Crear mi nueva clave de internet "<datos>"
    Then Usuario valida el mensaje de Felicitaciones has creado con exito tu clave cambio_clave "<datos>"
    And Usuario valida el correo de confirmacion de cambio de clave "<datos>"
    Examples:
          | datos |
          |     1 |

@NCD_Registro @HP
  Scenario Outline: Registro exitoso con Tarjeta en APP MiBanco
    Given Usuario se encuentra en la APP Mibanco registro "<datos>"
    When Usuario da tap al boton Registrate "<datos>"
    And Usuario da tap a registrarme con mi tarjeta de debito "<datos>"
    And Usuario ingresa su documento, tarjeta y clave de cajero registro "<datos>"
    And Usuario da tap en el boton Siguiente registro "<datos>"
    And Usuario extrae el otp del correo registro"<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Siguiente "<datos>"
    And Usuario ingresa la nueva clave de internet registro "<datos>" 
    And Usuario confirma la nueva clave de internet registro "<datos>" 
    And Usuario acepta los terminos y condiciones y da click en el boton Aceptar "<datos>"
    And Usuario da clik en el boton Crear mi nueva clave de internet registro"<datos>"
    Then Usuario valida el mensaje de Felicitaciones te registraste exitosamente "<datos>"
    And Usuario valida el correo de confirmacion de registro del cliente en NCD "<datos>"
    Examples:
      | datos |
      |     1 |


  @NCD_ActivarEnvioOtp @HP
  Scenario Outline: Activacion modo de confirmacion por correo APP MiBanco
    Given Usuario se encuentra logueado en la APP MiBanco "<datos>"
    And Usuario ingresa a las Opciones "<datos>"
    And Usuario da tap al boton modo de confirmacion "<datos>"
    When Usuario selecciona el modo de confirmacion por correo "<datos>"
    And Usuario extrae el otp del correo modoConfirmacion "<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Validar "<datos>"
    Then Usuario valida la activacion del modo confirmacion por correo "<datos>"
   
    Examples:
      | datos |
      |     1 |
