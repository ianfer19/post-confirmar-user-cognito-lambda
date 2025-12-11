from domain.exceptions import DomainValidationError
from utils.logger import get_logger

logger = get_logger(__name__)

class ConfirmSignupService:

    def __init__(self, cognito_repo):
        self.cognito_repo = cognito_repo

    def confirm(self, payload: dict):
        logger.info("Executing confirm signup service...")

        if "username" not in payload or "code" not in payload:
            raise DomainValidationError("username and code are required")

        username = payload["username"]
        code = payload["code"]

        return self.cognito_repo.confirm_user(username, code)
