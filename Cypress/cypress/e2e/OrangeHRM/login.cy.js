describe('orangeHRM Login Test Suite', () => {
    beforeEach (() => {
        cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    })
    it ('Login with invalid credentials', () => {
        cy.get('input[name="username"]').type('InvalidUser')
        cy.get('input[name="password"]').type('InvalidPass')
        cy.get('button[type="submit"]').click()
        cy.get('.oxd-alert-content').should('contain.text', 'Invalid credentials')
    })

    it ('Login with valid credentials', () => {
        cy.get('input[name="username"]').type('Admin')
        cy.get('input[name="password"]').type('admin123')
        cy.get('button[type="submit"]').click()
        cy.url().should('include', '/dashboard')
        cy.contains('Dashboard').should('be.visible')
    })

    
})