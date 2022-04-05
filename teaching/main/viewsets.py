from rest_framework import viewsets
from .serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
import json
from django.db.models import Sum, Count, F

class UsersViewset(viewsets.ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    @action(methods=['post'], detail=False)
    def login(self, request):
        if request.method == "POST":
            password = request.data['password']
            try:
                user = Users.objects.get(password=password)
                d = self.get_serializer_class()(user)
                return Response({'user': d.data}, status=200)
            except:
                return Response({'message': 'user not found'}, status=204)
        else:
            return Response()


class JobsViewset(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    # @action(methods=['post'], get)

class SectionViewset(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class ThemeViewset(viewsets.ModelViewSet):
    queryset = Theme.objects.all()
    serializer_class = ThemeSerializer 