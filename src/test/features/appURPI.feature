Feature: Flujos Automatizados APP URPI

  @Urpi @Calidad
  Scenario Outline: Login Exitoso del App URPI
    Given ingreso al App URPI "<datos>"
    When ingreso mi correo "<datos>"
    And doy click en el boton siguiente
    And ingreso la clave "<datos>"
    Then doy click en el boton ingresar

    Examples:
      | datos |
      |     1 |
      |     2 |
      |     3 |
