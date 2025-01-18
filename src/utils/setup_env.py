import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_env_variable(var_name: str, default=None):
    """Retrieve the value of an environment variable or return a default."""
    value = os.getenv(var_name, default)
    if value is None:
        raise EnvironmentError(f"Environment variable '{var_name}' is not set and no default value is provided.")
    return value

# Load specific variables
OPENSEA_API_KEY = get_env_variable("OPENSEA_API_KEY")
TEST_WALLET_1 = get_env_variable("TEST_WALLET_1")
TEST_WALLET_2 = get_env_variable("TEST_WALLET_2")

print(f"OPENSEA_API_KEY = {OPENSEA_API_KEY}")
print(f"TEST_WALLET_1 = {TEST_WALLET_1}")
print(f"TEST_WALLET_2 = {TEST_WALLET_2}")