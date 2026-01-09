describe('Login using fixtures', () => {

  beforeEach(() => {
    cy.fixture('user').as('data')
  })

  it('Valid login', function () {
    cy.login(this.data.validUser.username,
             this.data.validUser.password)
  })

  it('Invalid login', function () {
    cy.visit('https://opensource-demo.orangehrmlive.com/')
    cy.get('input[name="username"]').type(this.data.invalidUser.username)
    cy.get('input[name="password"]').type(this.data.invalidUser.password)
    cy.get('button[type="submit"]').click()

    cy.contains('Invalid credentials').should('be.visible')
  })
})
