"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import TrailImage, Image, Trail


class TrailImageView(ViewSet):
    
    def retrieve(self, request, pk):
        trailimage = TrailImage.objects.get(pk=pk)
        serializer = TrailImageSerializer(trailimage)
        return Response(serializer.data)
       
            


    def list(self, request):
        trailimages = TrailImage.objects.all()
        serializer = TrailImageSerializer(trailimages, many=True)
        return Response(serializer.data)
    

    def create(self, request):

        image = Image.objects.get(pk=request.data["image"])
        trail = Trail.objects.get(pk=request.data["trail"])

        trailimage = TrailImage.objects.create(
            image= image,
            trail= trail
            )
        serializer = TrailImageSerializer(trailimage)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class TrailImageSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = TrailImage
        fields = ('id', 'image', 'trail')
