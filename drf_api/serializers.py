from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Jobs


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Jobs
#         fields = ['job_title', 'min_salary', 'max_salary']

