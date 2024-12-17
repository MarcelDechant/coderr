from rest_framework.response import Response
from rest_framework.views import APIView
from authentication_app.api.serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken
from authentication_app.api.utils import receive_registration_data, receive_login_data

class LoginView(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request):
        data = receive_login_data(self.serializer_class(data=request.data))
        return Response(data)

class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        data = receive_registration_data(RegistrationSerializer(data=request.data))
        return Response(data)