from venv import logger
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserDetailsSerializer, UserDetailsLoginSerializer
from rest_framework import status
from .methods import encrypt_password
from .models import UserDetails


class SignUpAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserDetailsSerializer(data=data)
        print(serializer)
        if serializer.is_valid():
            raw_password = serializer.validated_data.get('password')
            encrypted_password = encrypt_password(raw_password)
            serializer.save(password=encrypted_password)
            return Response({'data': serializer.data, 'message': "User created successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPIView(APIView):
    def post(self, request):
        try:
            data = request.data
            email = data.get('email')
            password = data.get('password')

            user = UserDetails.objects.get(email=email)
            print(user)
            encryptPassword = encrypt_password(password)
            serializedUser = UserDetailsLoginSerializer(user)

            if user.password == encryptPassword:
                return Response(
                        {
                            "data": serializedUser.data,
                            "message": "User logged in successfully",
                        },
                        status=status.HTTP_200_OK,
                    )
            return Response(
                    {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
                )
            
        except UserDetails.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )

        except Exception as e:
            logger.error(e)
            return Response({"message": str(e)}, status=status.HTTP_502_BAD_GATEWAY)