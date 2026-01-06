# 🌳 Cypress Test Automation Framework

A modern end-to-end testing framework using Cypress for web application testing.

## 📋 Overview

This framework provides a structured approach to testing web applications using Cypress, featuring:
- Interactive test runner
- Real-time debugging capabilities
- Automatic waiting and intelligent retries
- Screenshot and video recording
- Comprehensive error reporting

## 🎯 Features

✅ Fast and reliable test execution  
✅ Easy-to-read test syntax  
✅ Time-travel debugging  
✅ Network request stubbing and spying  
✅ Cross-browser testing support  
✅ CI/CD integration ready  

## 📦 Installation

### Prerequisites
- Node.js 14.0+ 
- npm or yarn

### Setup Steps

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Verify Cypress installation:**
   ```bash
   npx cypress --version
   ```

## 🚀 Running Tests

### Interactive Mode (Cypress UI)
```bash
npx cypress open
```
This opens the Cypress Test Runner where you can see tests execute in real-time.

### Headless Mode (CLI)
```bash
npx cypress run
```
Run all tests in headless mode without the interactive UI.

### Run Specific Test File
```bash
npx cypress run --spec "cypress/e2e/path/to/test.cy.js"
```

### Run Tests in Specific Browser
```bash
npx cypress run --browser chrome
npx cypress run --browser firefox
npx cypress run --browser edge
```

## 📁 Project Structure

```
Cypress/
├── package.json
├── cypress.config.js         # Cypress configuration
├── cypress/
│   ├── e2e/                  # End-to-end test files
│   ├── support/              # Reusable commands and utilities
│   └── fixtures/             # Test data and mock responses
```

## 🔧 Configuration

Edit `cypress.config.js` to customize:
- Base URL
- Timeout values
- Screenshot/video settings
- Browser configurations
- Viewport sizes

## 📝 Writing Tests

### Basic Test Structure
```javascript
describe('Feature Name', () => {
  beforeEach(() => {
    cy.visit('https://example.com')
  })

  it('should perform an action', () => {
    cy.get('selector').click()
    cy.contains('Expected Text').should('be.visible')
  })
})
```

### Common Commands
```javascript
cy.visit(url)           // Navigate to a URL
cy.get(selector)        // Select an element
cy.click()              // Click an element
cy.type('text')         // Type into an input
cy.submit()             // Submit a form
cy.should('exist')      // Assert element exists
cy.wait(ms)             // Wait for time or request
cy.intercept()          // Spy or stub requests
```

## 🔍 Debugging

### Ways to Debug
1. **Cypress UI** - Use the interactive test runner with time-travel debugging
2. **Browser DevTools** - Right-click and inspect elements during test run
3. **`.debug()`** - Add this method to pause and inspect
4. **Logs** - Check console output for test information

### Example:
```javascript
cy.get('button').debug().click()
```

## 📸 Screenshots & Videos

Cypress automatically captures:
- **Screenshots** - On test failure (in `cypress/screenshots/`)
- **Videos** - Of entire test run (in `cypress/videos/`)

Disable in `cypress.config.js`:
```javascript
video: false,
screenshotOnRunFailure: false
```

## 🌐 Testing Websites

Practice and demo sites for testing:
- [SauceDemo](https://www.saucedemo.com/)
- [The Internet (Heroku)](https://the-internet.herokuapp.com/)
- [Cypress Kitchen Sink](https://example.cypress.io/)

## 🔄 CI/CD Integration

### GitHub Actions Example
```yaml
name: Cypress Tests
on: [push, pull_request]
jobs:
  cypress:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-node@v2
        with:
          node-version: 16
      - run: npm install
      - run: npx cypress run
```

## 📚 Resources

- [Cypress Official Documentation](https://docs.cypress.io/)
- [Best Practices](https://docs.cypress.io/guides/references/best-practices)
- [API Reference](https://docs.cypress.io/api/table-of-contents)

## 🤝 Contributing

Contributions are welcome! Please ensure:
- Tests follow the existing code style
- New tests include descriptive comments
- All tests pass before submitting PR

## 📄 License

ISC License

---

**Happy Testing with Cypress! 🎉**