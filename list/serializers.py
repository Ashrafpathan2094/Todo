from rest_framework import serializers

from list.models import Lists

class ListsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lists
        fields = ('id','title','description','done',)