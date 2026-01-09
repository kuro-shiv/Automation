const { defineConfig } = require("cypress");

module.exports = defineConfig({
  projectId: 'zdex8f',
  e2e: {
    setupNodeEvents(on, config) {
      // implement node event listeners here
    },
  },
});
