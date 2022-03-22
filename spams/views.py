from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from spams.serializers import (UserSerializer)
from spams.models import User, Contact

from rest_framework.permissions import IsAuthenticated
from django.db.models import Q

# Create your views here.

class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user = serializer.validated_data
        return Response(message="successful", status=status.HTTP_201_CREATED)


#this allow user to create user phone number, add a new to contact
class UserContact(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        phone_num = request.data['phone_number']
        name = request.data['name']
        user = request.user
        contact = User.objects.filter(phone_number=phone_num).first()
        if not contact:
            contact = User.objects.create(phone_number=phone_num)
            return Response({"message":"user successful created"}, status=status.HTTP_201_CREATED)
        user_contact = Contact.objects.filter(main_user=user, added_contact=contact).first()
        if not user_contact:
            Contact.objects.create(main_user = user, added_contact=contact, contact_name=name)
            return Response({"message":"contact successful created"}, status=status.HTTP_201_CREATED)
        

#this allow logged in user to add a phonr number to spam, 
# if it extist, mark it as spam, else create a new user and mark it as spam
class Spams(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        phone_num = request.data['phone_number']
        user = User.objects.filter(phone_number=phone_num).first()
        if user:
            user.is_spam = True
            user.save()
            return Response({"message":"user marked as spam"}, status=status.HTTP_201_CREATED)
        else:
            User.objects.create(
        phone_number=phone_num,
        is_spam = True
        )
            return Response({"message":"user successful created and marked as spam"}, status=status.HTTP_201_CREATED)


#this search global database by phone_number
class SearchNumber(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        if query :
            user = User.objects.filter(phone_number=query)
            if user:
                serializer = UserSerializer(user, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Phone number does not exist"}, status=status.HTTP_400_BAD_REQUEST)


#this search global database by name
class SearchName(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        query = request.GET.get('q', '')
        if query :
            users = User.objects.filter(name=query)
            if users:
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"message": "Name does not exist"}, status=status.HTTP_400_BAD_REQUEST)
        