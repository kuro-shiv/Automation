describe('Dashboard Validation',() => {
    beforeEach (() => {
        cy.login('Admin','admin123')
    })
    it ('Validate Dashboard Elements', () => {
        cy.contains('Time at Work').should('be.visible')
        cy.contains('Quick Launch').should('be.visible')
    })
})