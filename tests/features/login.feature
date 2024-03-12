Feature:
    As a user
    I want to login to my account
    so that I can browse the application

    Scenario: User logs in successfully
        Given user navigates to Login Page
        When enters the correct credentials
        Then user is successfully logged in

    # Scenario: User fails to log in with the wrong credentials
    # Write the steps for this scenario
