Feature: Flujos Automatizados APP TEST

  @Test @Calidad
  Scenario Outline: Registro App Test
    Given usuario ingresa a la app TEST "<datos>"
    And usuario da click en boton Registrarse
    And usuario ingresa datos de formulario "<datos>"
    And usuario se Registra
    Then se verifica el registro

    Examples:
      | datos  | 
      | 1      |
      | 2      |
      | 3      |
