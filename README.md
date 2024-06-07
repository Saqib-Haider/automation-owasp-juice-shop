# automation-owasp-juice-shop

This respository contains automation for owasp juice shop.
Best to run API Automation first and then Run UI Automation

**Pre-requisite**: Ensure python3 installed and postman downloaded

**API Automation**

API Automation is done with Postman tool along with Newman for reporting.
A clean up request is added to maintain stateless behaviour of entire automation.

To run, simply clone and export the collection and environment variable. Then run the Scenarios

OR

Simply to run with newman, 


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

```


**UI Automation**


UI automation tests for OWASP Juice Shop using Playwright and Pytest, organized in accordance with the Page Object Model (POM) design pattern. It includes setup instructions, usage examples, and information on CI/CD integration with GitHub Actions and reporting with Allure.

1. Install the requirement.txt file
```
pip install -r requirements.txt
```

4. Then run the test cases

```
pytest testcases
```
