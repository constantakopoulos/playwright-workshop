Introduction
------------

### What is a test framework?

A test framework is a set of guidelines or rules used for creating and designing test cases. In python, one of the most popular test frameworks is *pytest*.

### Key Features

1.  **Test Case Management:** A framework allows the organization and management of test cases, making it easier to create, maintain, and execute them.

2.  **Fixture Setup and Teardown:** It provides mechanisms for setting up preconditions (fixtures) before tests run and cleaning up afterward, ensuring a consistent test environment.

3.  **Test Execution:** The framework facilitates the execution of test cases and the collection of results, often supporting parallel test execution for efficiency.

4.  **Assertions:** A set of predefined assertions or validation methods are typically included in a test framework for verifying expected outcomes and ensuring that the software behaves as intended.

5.  **Reporting:** Test frameworks often generate detailed reports summarizing test results, making it easier to identify and analyze issues.

6.  **Parameterization:** Frameworks may support the parameterization of test inputs, allowing tests to be run with different sets of data.

7.  **Test Data Management:** It may provide tools for managing test data, such as creating and maintaining test databases or handling data-driven testing.

**Setup**
---------

First, clone the project in your computer using:

git clone <>

If you don't have poetry in your system run pip install poetry to get it.

Then, inside the project's root folder, run poetry install.

1.1 Simple test cases
---------------------

git checkout chapter1.1-simple-tests

### Test Collection

Pytest uses a few naming conventions for discovering and collecting tests

-   Test file names and test functions should start with the prefix "test_"

-   Test Classes should start with the prefix "Test"

These default conventions can be changed in the pytest.ini file.

### Test structure/grouping

Usually, we group the tests by the features they are testing. This means that all the tests for the same feature go inside one file. This is not something strict though, each team could have variations of this approach as long as there is a reason behind the decision.

1.2 Pytest fixtures
-------------------

git checkout chapter1.2-fixtures

Pytest fixtures are **a way of providing data, test doubles, or state setup to your tests**. Fixtures are functions that can return a wide range of values. Each test that depends on a fixture must explicitly accept that fixture as an argument.

Remember!\
Fixtures are not supposed to have parameters. Think of them as "fixed" components to assist your tests.

### [Fixture Scope](https://docs.pytest.org/en/6.2.x/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session)

There are 5 available scopes: function(default), class, module, package, session\
The scope of a fixture configures when the fixture will be executed. If set to "function" it will be executed once per function, if set to "session" it will be executed once per test session, and so on.

### [Teardown/Cleanup](https://docs.pytest.org/en/6.2.x/fixture.html#teardown-cleanup-aka-fixture-finalization)

yield keyword can be used to run code at the end of a fixture's scope (after a test function, test class, test session, etc). Check the documentation for examples.

### [Conftest](https://docs.pytest.org/en/6.2.x/fixture.html#conftest-py-sharing-fixtures-across-multiple-files)

git checkout chapter1.2-conftest

A conftest.py can be used to share common fixtures between your tests across a directory.\
[Pytest hooks](https://docs.pytest.org/en/7.1.x/how-to/writing_hook_functions.html) can also be placed there. In general, it is a file to put all the configurations of pytest.

#### Where

Usually, the "conftest" file is placed in the same directory as the test files.

**Multiple "conftest" files**\
"Conftest" files apply across a directory. This means that you can have multiple "conftest" files in case you want to have different pytest configurations across different directories, for example, different settings for UI and API tests.

1.3 Page Objects Model
----------------------

git checkout chapter1.3-login-page and then git checkout chapter1.3-base-page

**Page Object Model (POM)** is a design pattern, popularly used in test automation that creates Object Repository for web UI elements. The advantage of the model is that it reduces code duplication and improves test maintenance.

### Understand the 3 layers

### Layer 1: Basic Browser Actions

All browsers share common functionalities and actions that the user can perform. For example:

-   click

-   enter text in a field

-   scroll up/down

-   navigate to a page

-   etc

Consequently, every automation framework (Selenium, Playwright, or any other) should have an API to implement these basic actions.

The point here is to create a single location where all the browser actions will live and the UI framework's (e.g. Playwright) API will be integrated. This way our framework becomes more maintainable and more scalable for the future.

### Layer 2: Page Objects or Components

Here, we create groups of locators and actions that belong to the same page or component. This way, whenever a button changes we only have to update it in a single location.

In this layer, we use the browser actions from Layer 1. We don't want to use directly the Playwright's/Selenium's API. This way, any updates in our "browser engine" should take place only in Layer 1.\
For example, it makes sense to create a "Login" page object and have the following inside it:

-   Locators: username field, password field, submit button

-   Actions: fill in the username, fill in the password, click the submit button, read the error message

### Layer 3: Test Scripts

All tests consist of three stages: Arrange (setup), Act, Assert

Every component or information required for executing the test should be gathered here. This may include test data, fixtures, page objects, and many other things necessary for the test.

Most importantly, the assertions should take place in this layer

In this layer, we use the page actions from Layer 2. We don't want to use stuff directly from Layer 1.

1.4 Env files and Sensitive data
--------------------------------

git checkout chapter1.4-env-files

When developers create software, they often need to use sensitive information like passwords, API keys, or other configuration settings. However, it's not a good practice to hardcode these values directly into the source code. Why? Because if someone gains access to the code, they could easily see and misuse this sensitive information.

Here's where the .env file comes in:

1.  **Security:** The .env file provides a way to store sensitive information separately from the code. This file is not shared publicly or included in the code repository, so it's more secure.

2.  **Flexibility:** The .env file allows developers to change configuration settings without modifying the actual code. This makes it easier to adapt the software to different environments (like development, testing, or production) without altering the codebase.

3.  **Portability:** Since the .env file contains configuration information, it can be easily moved or shared with other developers. This makes it simpler to deploy the software in different locations or on different servers without exposing sensitive details in the code.

In summary, the .env file acts as a secure and flexible way for developers to manage sensitive information and configuration settings without embedding them directly into the code. It's like a separate, private note that the program refers to when it needs specific instructions or secrets.

The .env should NOT be committed with the rest of our code and uploaded to GitHub/BitBucket. That's why it's necessary to include it in the .gitignore file.

.env can be used for any kind of configuration related to the environment, not only for secrets.

[Optional] Reporting
--------------------

Pytest has a great plugin ecosystem which makes it very flexible and can be extended with many extra features.

**HTML Reports**

pytest-html is a nice pytest plugin to generate HTML reports.

Installation: pip install pytest-html

Usage: pytest --html=report.html --self-contained-html

You can read more in the docs [here](https://pytest-html.readthedocs.io/en/latest/index.html).

Of course, there are many other options to generate test reports in various formats (json, xml, and more) using the appropriate plugin. For example, in our projects, we use extensively the "allure reports" plugin.