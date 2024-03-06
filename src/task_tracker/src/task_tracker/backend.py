from social_core.backends.oauth import BaseOAuth2


class PopugOAuth2Backend(BaseOAuth2):
    name = 'popug_oauth2'
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/o/authorize'
    ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/o/token'
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    STATE_PARAMETER = False
    ID_KEY = 'qp4SJzLlDjo6WuZPzP1sAkfjt2UOmGu6RW7irxwN'

    def get_user_details(self, response):
        return {
            'email': response.get('email'),
            'public_id': response.get('public_id'),
        }

    def user_data(self, access_token, *args, **kwargs):
        return self.get_json(
            'http://127.0.0.1:8000/o/userinfo',
            headers={'Authorization': 'Bearer ' + access_token}
        )
