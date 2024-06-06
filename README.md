# automation-owasp-juice-shop

This projects contains automation for owasp juice shop.
Best to run API Automation first and then Run UI Automation

**Pre-requisite**: Ensure python3 installed and postman downloaded
1. API Automation is done with Postman tool along with Newman for reporting.
To run, simply clone and export the collection and environment variable. Then run the Scenarios
A clean up request is added to maintain stateless behaviour of entire automation.

2. UI Automation is done with Playwright,Pytest framework along with allure reporting. Also following generic Page Object Model format.
```
pip install -r requirements.txt
```

then run the test cases

```
pytest testcases
```
