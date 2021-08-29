from rest_framework import serializers
from .models import Task
 
class NewTaskSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name="base:user-detail")
    class Meta:
        model = Task
        fields = ['title', 'description', 'complete' ,'priority','dueDate','assignUser']