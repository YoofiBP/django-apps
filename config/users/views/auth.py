from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from ..models import User


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
        access_token = RefreshToken.for_user(user)
        return Response(status=status.HTTP_200_OK, data={
            'token': str(access_token.access_token)
        })
