from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken

class RefreshAccessTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response.status_code == 401:
            refresh_token = request.COOKIES.get('refresh_token')
            if refresh_token:
                try:
                    new_access_token = RefreshToken(refresh_token).access_token
                    response.set_cookie(
                        key='access_token',
                        value=str(new_access_token),
                        httponly=True,
                        samesite='Lax'
                    )
                    response.data['access_token'] = str(new_access_token)
                    response.status_code = 200
                except (InvalidToken, TokenError):
                    response.data = {'error': 'Invalid token'}
                    response.status_code = 401

        return response

class AccessTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get('access_token')
        if access_token:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'

        response = self.get_response(request)
        return response