describe('orangeHRM Login Test Suite', () => {
cy.visit('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
cy.login('Admin','admin123')
})