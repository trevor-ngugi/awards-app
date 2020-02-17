from rest_framework import serializers
from .models import Profile,Projects,ratings


class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('title', 'description', 'project_image','link','name','pub_date')