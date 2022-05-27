from users.models import User
from users.serializers import UserSerializer

serializer = UserSerializer(data={'name': 'Yoofi', 'email': 'email@email.com', 'password': 'password'});
