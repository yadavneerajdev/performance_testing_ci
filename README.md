# Test CI

A simple Node.js application with automated performance testing using Lighthouse CI.

## Setup

1. Clone the repository
2. Run `npm install`
3. Run `npm start` to start the server
4. Run `npm run lhci` to run performance tests locally

## Performance Testing

This project uses Lighthouse CI to automate performance testing. The workflow runs on every push and pull request to the main branch.

The tests check:

- Performance score >= 0.9
- Accessibility score >= 0.9
- Best practices score >= 0.9
- SEO score >= 0.9

## GitHub Workflow

The `.github/workflows/performance.yml` file defines the CI pipeline that:

- Sets up Node.js
- Installs dependencies
- Runs Lighthouse CI tests
