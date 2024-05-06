Feature: Flujos Automatizados APP TEST

  @Test1
  Scenario Outline: Registro App Test
    Given usuario ingresa a la app TEST
    And usuario da click en boton Registrarse
    And usuario ingresa datos de formulario "<nombre>", "<id>", "<pass1>", "<pass2>"
    And usuario se Registra
    Then se verifica el registro

    Examples:
      | nombre         | id          | pass1      | pass2      |
      | Abraham Rivera | arivera2024 | 1234567890 | 1234567890 |
