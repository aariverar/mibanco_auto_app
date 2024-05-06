Feature: Flujos Automatizados URPI

  @Prueba1
  Scenario Outline: Login Exitoso del App URPI
    Given ingreso al App URPI
    When ingreso mi correo "<correo>"
    And doy click en el boton siguiente
    And ingreso la clave "<password>"
    Then doy click en el boton ingresar

    Examples: 
      | correo                  | password  |
      | 61444tmp@mibanco.com.pe | Mibanco$4 |
