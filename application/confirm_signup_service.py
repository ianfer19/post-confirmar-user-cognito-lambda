from domain.exceptions import DomainValidationError
from utils.logger import get_logger

logger = get_logger(__name__)

class ConfirmSignupService:

    def __init__(self, cognito_repo):
        self.cognito_repo = cognito_repo

    def confirm(self, payload: dict):
        logger.info("Executing confirm signup service...")

        username = payload.get("username", "").strip()
        code = payload.get("code", "").strip()

        if not username or not code:
            raise DomainValidationError("username and code are required and cannot be empty")

        logger.info(f"Confirming user with username={username}")

        return self.cognito_repo.confirm_user(username, code)
