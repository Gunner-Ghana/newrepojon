from rest_framework import serializers 
from tutorials.models import AccountMove
 
 
class TutorialSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = AccountMove
        fields = ('id','name',
                  )