from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken
from django.core.cache import cache
from ..models import User
from ..serializers import UserSerializer


@api_view(['POST'])
def signin(request):
    if request.method == 'POST':
        email = request.data['email']
        password = request.data['password']

        try:
            user = User.objects.get(email=email)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        if not check_password(password=password, encoded=user.password):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        access_token = AccessToken.for_user(user)
        return Response(status=status.HTTP_200_OK, data={
            'token': str(access_token),
            'userInDb': UserSerializer(user).data
        })


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def sign_out(request):
    if request.method == 'GET':
        token = str(request.auth)
        expired_tokens = cache.get('expiredTokens')
        if expired_tokens is None:
            expired_tokens = []
        if token not in expired_tokens:
            print('here')
            expired_tokens.append(token)
        cache.set('expiredTokens', expired_tokens, timeout=3600)
        return Response(status=status.HTTP_200_OK)
