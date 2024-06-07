# automation-owasp-juice-shop

This projects contains automation for owasp juice shop.
Best to run API Automation first and then Run UI Automation

**Pre-requisite**: Ensure python3 installed and postman downloaded
1. API Automation is done with Postman tool along with Newman for reporting.
To run, simply clone and export the collection and environment variable. Then run the Scenarios
A clean up request is added to maintain stateless behaviour of entire automation.

**API Automation**
Simply to run witth newman, 
1. Install nodejs
2. Install newman
  ```
  npm install -g newman
  ```
3. Install html-exta for reporting
 ```
   npm install -g newman-reporter-htmlextra
 ```
4. Run the collection, ensure that the working directory is API Automation
```
  newman run Automation OWASP Juice Shop.postman_collection.json -e OWASP Juice Shop Environment.postman_environment.json -r htmlextra 
.

```

**UI Automation**
UI Automation is done with Playwright,Pytest framework along with allure reporting. Also following generic Page Object Model format.
```
pip install -r requirements.txt
```

Then run the test cases

```
pytest testcases
```

Added GitHub Action for CI/CD environment workflow for UI Automation
