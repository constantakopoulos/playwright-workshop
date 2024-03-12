# Playwright Workshop - Part 2

Topics to be covered:
- Test framework: pytest
- BDD in test automation

## Setup
Clone the repository
`git clone git@github.com:constantakopoulos/playwright-workshop.git`

Install "poetry" in your system
`pip install poetry`

Activate virtual env
`poetry shell`"

Install the dependencies of the project
`poetry install`

## Follow along
Each part of the workshop's code is on a different git branch. If you follow the confluence page of the workshop there are instructions about which branch you need to checkout in every section.

## References
Setup the project
1. Git
First, make sure “git” is installed on your machine.

[How to install git]([url](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git))

2. Git & GitHub
Feel free to skip it if you have already set up git and GitHub.

You should configure “git” to work with GitHub. Here is a good guide → Your first time with Git and GitHub

3. Download the project
Go to (or create) the folder where you store all your coding projects.

Then, download the workshop’s code from GitHub with the command:

git clone https://github.com/geokats7/playwright-workshop-v2.git

Now, you should have the workshop’s code locally, on your machine. Open the folder with PyCharm or any other code editor.

Run the following command to follow along with the first chapter:

git checkout chapter1.1-simple-tests

4. Install project dependencies
First, you have to install poetry to your system.

Run pip install poetry to get the latest version of poetry.

Then, inside the project’s root folder, run:

poetry install

This command will create a virtual environment and install all the required dependencies (located in the pyproject.toml file) in it.

Playwright
Run playwright install or python -m playwright install to install all the dependencies of the playwright framework.
