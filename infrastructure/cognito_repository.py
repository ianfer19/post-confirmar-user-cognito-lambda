import boto3
from botocore.exceptions import ClientError
from domain.exceptions import CognitoError
from utils.logger import get_logger

logger = get_logger(__name__)

class CognitoRepository:

    def __init__(self, client_id):
        self.client = boto3.client("cognito-idp")
        self.client_id = client_id

    # Método existente para signup...
    # def signup_user(...)

    def confirm_user(self, username: str, code: str):
        try:
            logger.info(f"Confirming Cognito user {username}...")

            self.client.confirm_sign_up(
                ClientId=self.client_id,
                Username=username,
                ConfirmationCode=code
            )

            logger.info("User successfully confirmed.")

            return {"username": username, "message": "User confirmed."}

        except ClientError as e:
            logger.error(str(e))
            raise CognitoError(e.response["Error"]["Message"])
