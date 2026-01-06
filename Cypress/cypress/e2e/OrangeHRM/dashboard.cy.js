describe('Dashboard Validation',() => {
    beforeEach (() => {
        cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
        cy.get('input[name="username"]').type('Admin')
        cy.get('input[name="password"]').type('admin123')
        cy.get('button[type="submit"]').click()
        cy.url().should('include', '/dashboard')
    })
    it ('Validate Dashboard Elements', () => {
        cy.contains('Time at Work').should('be.visible')
        cy.contains('Quick Launch').should('be.visible')
    })
})