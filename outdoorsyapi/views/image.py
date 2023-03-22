"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import Image


class ImageView(ViewSet):
    
    def retrieve(self, request, pk):
        image = Image.objects.get(pk=pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)
       
            


    def list(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)
    

    def create(self, request):

        image = Image.objects.create(
            image= request.data["image"]
            )
        serializer = ImageSerializer(image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
class ImageSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = Image
        fields = ('id', 'image')
