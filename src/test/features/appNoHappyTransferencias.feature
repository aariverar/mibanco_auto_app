Feature: Flujos No Happy - Transferencias Mibanco APP

  @NCD_TransferenciaOtrasCuentas @NHP @TransfNHP
  Scenario Outline: Transferencias a otras cuentas - validacion menos del limite minimo
    Given Usuario se encuentra logueado en la APP MiBanco transf NHP "<datos>"
    And Usuario ingresa a la opcion de Transferencias y da tap en A otras cuentas de Mibanco "<datos>"
    When Usuario selecciona la cuenta origen transferencias_otras_cuentas "<datos>"
    And Usuario ingresa la cuenta destino transferencias_otras_cuentas "<datos>"
    And Usuario selecciona el tipo de moneda transferencias_otras_cuentas "<datos>"
    And Usuario ingresa menos del monto minimo a transferir "<datos>"
    Then Usuario valida el mensaje de error "el monto debe ser mayor o igual a"

    Examples:
      | datos |
      |     1 |
      |     2 |
      |     3 |
      |     4 |

  @NCD_TransferenciaCuentasPropias @NHP @TransfNHP
  Scenario Outline: Transferencias a otras cuentas - validacion más del limite maximo
    Given Usuario se encuentra logueado en la APP MiBanco transf NHP "<datos>"
    And Usuario ingresa a la opcion de Transferencias y da tap en A otras cuentas de Mibanco "<datos>"
    When Usuario selecciona la cuenta origen transferencias_otras_cuentas "<datos>"
    And Usuario ingresa la cuenta destino transferencias_otras_cuentas "<datos>"
    And Usuario selecciona el tipo de moneda transferencias_otras_cuentas "<datos>"
    And Usuario ingresa menos del monto minimo a transferir "<datos>"
    Then Usuario valida el mensaje de error "el monto debe ser menor o igual a"

    Examples:
      | datos |
      |     5 |
      |     6 |
      |     7 |
      |     8 |