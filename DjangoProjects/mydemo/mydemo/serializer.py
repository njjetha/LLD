from rest_framework import serializers
from mydemo.models import User,Student

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields="__all__"

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model=Student
        fields="__all__"