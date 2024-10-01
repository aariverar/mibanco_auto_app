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
      |     3 |
     # |     2 |      

  @NCD_ActivarEnvioOtp @HP @Ejecucion1
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

  @NCD_TransferenciaOtrasCuentas @NCD_HAPPY_PATH
  Scenario Outline: Transferencias exitosa a otras cuentas Mibanco APP
    Given Usuario se encuentra logueado en la APP MiBanco transf "<datos>"
    And Usuario ingresa a la opcion de Transferencias y da tap en A otras cuentas de Mibanco "<datos>"
    When Usuario selecciona la cuenta origen transferencias_otras_cuentas "<datos>"
    And Usuario ingresa la cuenta destino transferencias_otras_cuentas "<datos>"
    And Usuario selecciona el tipo de moneda transferencias_otras_cuentas "<datos>"
    And Usuario ingresa el monto a transferir "<datos>"
    And Usuario da tap en el boton Siguiente transferencias_otras_cuentas "<datos>"
    And Usuario verifica informacion de la transferencia "<datos>"
    And Usuario extrae el otp del correo "<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Validar transferencias_otras_cuentas "<datos>"
    Then Usuario valida la constancia de transferencia exitosa transferencias_otras_cuentas "<datos>"

    Examples:
      | datos |
      |     1 |
      |     2 |

  @NCD_TransferenciaCuentasPropias @NCD_HAPPY_PATH
  Scenario Outline: Transferencias exitosa entre cuentas propias Mibanco APP
    Given Usuario se encuentra logueado en la APP MiBanco transfPropias "<datos>"
    And Usuario ingresa a la opcion de Transferencias y da tap en Entre mis cuentas Mibanco "<datos>"
    And Usuario selecciona la cuenta origen entre_mis_cuentas "<datos>"
    And Usuario selecciona la cuenta destino entre_mis_cuentas "<datos>"
    And Usuario ingresa el monto a transferir "<datos>"
    And Usuario da tap en el boton Siguiente transfPropias "<datos>"
    And Usuario verifica informacion de la transferencia Propia "<datos>"
    And Usuario da click en el boton transferir "<datos>"
    Then Usuario valida la constancia de transferencia exitosa transfPropias"<datos>"

    Examples:
      | datos |
      |     1 |

  @NCD_AperturaCta_DNI @HP @Ejecucion1
  Scenario Outline: Apertura de Cuenta de clientes con DNI Mibanco APP
    Given Usuario se encuentra logueado en la APP MiBanco apertura "<datos>"
    When Usuario ingresa a Abre tu cuenta de Ahorros aqui "<datos>"
    And Usuario selecciona el tipo de cuenta "<datos>"
    And Usuario selecciona el tipo de moneda "<datos>"
    And Usuario da click en el boton Abrir cuenta del paso 1 "<datos>"
    And Usuario da click en el boton Entiendo de la ventana modal "<datos>"
    And Usuario acepta los terminos y condiciones y residencia fiscal "<datos>"
    And Usuario da click en el boton Abrir cuenta del paso 2 "<datos>"
    And Usuario extrae codigo de otp desde su correo "<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Validar 2 "<datos>"
    Then Usuario valida la constancia de creacion de cuenta exitosa "<datos>"
    And Usuario ingresa a su correo outlook y da click en el ultimo correo recibido apertura "<datos>"
    And Usuario valida el correo de confirmacion de apertura de cuenta "<datos>"

    Examples:
      | datos |
     # |     1 |
      |     2 |

@NCD_CancelarCuenta @HP
  Scenario Outline: Cancelacion de cuenta Mibanco APP
    Given Usuario se encuentra logueado en la APP MiBanco cancelacion "<datos>"
    When Usuario selecciona la cuenta a cancelar "<datos>"
    And Usuario da tap en el boton de Cancelar Cuenta "<datos>"
    And Usuario da tap en el boton Si cancelar de la ventana modal "<datos>"
    And Usuario visualiza la pantalla de confirmacion de cancelacion de cuenta "<datos>"
    And Usuario de tap al boton confirmar "<datos>"
    And Usuario extrae el otp del correo "<datos>"
    And Usuario ingresa el codigo otp y da click en el boton Validar 2 "<datos>"
    Then Usuario valida la costancia de cancelacion de cuenta "<datos>"
  
    Examples:
      | datos |
      |     1 |