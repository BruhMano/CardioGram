from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class RefreshAccessTokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get('access_token')
        if access_token:
            try:
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {access_token}'
                jwt_auth = JWTAuthentication()
                jwt_auth.get_validated_token(access_token)
            except (InvalidToken, TokenError):
                refresh_token = request.COOKIES.get('refresh_token')

                if refresh_token:
                    try:
                        new_access_token = RefreshToken(refresh_token).access_token
                        request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'
                        response = self.get_response(request)
                        response.set_cookie(
                            key='access_token',
                            value=str(new_access_token),
                            httponly=True,
                            samesite='Lax'
                        )
                        response.status_code = 200
                        return response
                    except (InvalidToken, TokenError):
                        response.data = {'error': 'Invalid refresh token. You need to login again!'}
                        response.status_code = 401
                        response.delete_cookie('refresh_token')
                        response.delete_cookie('access_token')
                        return response
        response = self.get_response(request)
        return response