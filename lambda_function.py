import json
import os
from application.confirm_signup_service import ConfirmSignupService
from infrastructure.cognito_repository import CognitoRepository
from utils.response import success, error
from domain.exceptions import DomainValidationError, CognitoError
from utils.logger import get_logger

logger = get_logger(__name__)

CLIENT_ID = os.environ["CLIENT_ID"]

cognito_repo = CognitoRepository(CLIENT_ID)
confirm_service = ConfirmSignupService(cognito_repo)

def lambda_handler(event, context):
    logger.info("ConfirmSignup Lambda invoked")

    try:
        body = json.loads(event.get("body", "{}"))

        result = confirm_service.confirm(body)
        return success(result, 200)

    except DomainValidationError as e:
        return error(str(e), 400)

    except CognitoError as e:
        return error(str(e), 400)

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return error("Internal server error", 500)
