Introduction
------------

Behavior-Driven Development (BDD) is a collaborative approach to software development and testing that prioritizes communication between teams. By using a common language for executable specifications, BDD aligns technical and non-technical stakeholders, fostering a shared understanding of system behaviors.

One side-effect of applying BDD to a test framework is that it can work as documentation as well. This has been proven quite useful in projects where the test scenarios are very complex.

### Gherkin language

Normally, BDD is written using the "Gherkin Language", a domain-specific language serving as a structured format for defining test cases and executable specifications. Gherkin is designed to be both human-readable and machine-executable. Its syntax employs plain language constructs such as Given, When, Then.

-   **Given:** Sets the initial context or preconditions for a scenario. It outlines the starting state of the system before a specific action takes place.

-   **When:** Describes the action or event that triggers a particular behavior. It represents the specific operation or input that the system undergoes, often the key event being tested.

-   **Then:** Defines the expected outcome or result after the action specified in the "When" clause. It articulates the expected behavior or the state the system should be in following the execution of the specified action.

[What is BDD Testing? A Complete Guide](https://katalon.com/resources-center/blog/bdd-testing)

2.1 Pytest-BDD
--------------

pytest-bdd is a pytest plugin that works a BDD framework for pytest. We chose this package because under the hood we still use pytest to run our test suites. This means that everything we learned so far still applies and there is no need to invest in another standalone test framework like "behave".

### Test Structure

-   **Feature files:** Wherer the BDD scenarios are written

-   **Step definition files:** Where the actual test code in python is written

For pytest-bdd the step definition files are considered to be the "test" files, not the feature files!

### Adding the extra BDD layer

Now our framework consists of the following layers. A new BDD layer has been added on top to host the feature files. Also, the test script files are now "step definition" files where the test code is hosted.

Other than that, nothing else is affected.

[PyTest --- BDD (Behavioural Driven Development)](https://medium.com/@ramanish1992/pytest-bdd-behavioural-driven-development-a5df4d90619a)
