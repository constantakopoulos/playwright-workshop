import os

from dotenv import load_dotenv

load_dotenv()

ENVIRONMENTS = {
    "staging": {
        "client_url": "https://practicetestautomation.com/practice-test-login/",
    },
}


class AppEnvSettings:
    def __init__(self, environment: str = "staging"):
        self.environment = environment
        self.client_url = os.getenv("CLIENT_URL") or self._get_env_settings_dict().get("client_url")
        self.login_user = os.getenv("LOGIN_USERNAME")
        self.login_password = os.getenv("LOGIN_PASSWORD")

    def _get_env_settings_dict(self) -> dict:
        """
        Get all environment related settings in a dictionary.
        In case of review apps raises a KeyError and the except
        clause is executed.
        """
        try:
            return ENVIRONMENTS[self.environment]
        except KeyError:
            raise KeyError(f"Environment {self.environment} not found")
