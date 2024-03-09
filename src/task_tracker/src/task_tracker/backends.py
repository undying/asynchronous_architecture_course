import hashlib
import os
import base64
import logging

from social_core.backends.oauth import BaseOAuth2


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class PopugOauth2(BaseOAuth2):
    name = "popug_oauth2"
    AUTHORIZATION_URL = "http://127.0.0.1:8000/o/authorize/"
    ACCESS_TOKEN_URL = "http://127.0.0.1:8000/o/token/"
    ACCESS_TOKEN_METHOD = "POST"
    SCOPE_SEPARATOR = ","
    EXTRA_DATA = []

    def get_code_challenge(self):
        code_verifier = base64.urlsafe_b64encode(os.urandom(32)).rstrip(b"=")
        code_challenge = base64.urlsafe_b64encode(hashlib.sha256(code_verifier).digest()).rstrip(b"=")
        self.strategy.session['code_verifier'] = code_verifier.decode("utf-8")
        return code_challenge.decode("utf-8")

    def auth_params(self, state=None):
        params = super().auth_params(state)
        code_challenge = self.get_code_challenge()

        params["code_challenge"] = code_challenge
        params["code_challenge_method"] = "S256"

        return params

    def get_code_verifier(self):
        return self.strategy.session.get("code_verifier", None)

    def auth_complete_params(self, state=None):
        params = super().auth_complete_params(state=state)

        code_verifier = self.get_code_verifier()
        params["code_verifier"] = code_verifier

        return params

    def get_user_details(self, response):
        return {"email": response.get("email")}

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json("http://127.0.0.1:8000/api/userinfo/", headers={"Authorization": "Bearer " + access_token})
