"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import Trail


class TrailView(ViewSet):
    
    def retrieve(self, request, pk):
        trail = Trail.objects.get(pk=pk)
        serializer = TrailSerializer(trail)
        return Response(serializer.data)
       
            


    def list(self, request):
        trails = Trail.objects.all()
        serializer = TrailSerializer(trails, many=True)
        return Response(serializer.data)
    

    def create(self, request):

        trail = Trail.objects.create(
            name= request.data["name"],
            description=request.data["description"],
            length = request.data["length"]
            )
        serializer = TrailSerializer(trail)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    
class TrailSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = Trail
        fields = ('id', 'name', 'description', 'length')
