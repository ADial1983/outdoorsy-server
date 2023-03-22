"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import Rating, Trail


class RatingView(ViewSet):
    
    def retrieve(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        serializer = RatingSerializer(rating)
        return Response(serializer.data)
       
            


    def list(self, request):
        if "trail" in request.query_params:
            ratings = Rating.objects.filter(trail_id=request.query_params['trail'])
        else: 
            ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)
    
    def create(self, request):

        trail = Trail.objects.get(pk=request.data["trail"])

        rating = Rating.objects.create(
            user= request.auth.user,
            trail= trail,
            bathroom = request.data["bathroom"],
            parking = request.data["parking"],
            width = request.data["width"],
            clear = request.data["clear"],
            steep = request.data["steep"]
            )
        serializer = RatingSerializer(rating)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        trail = Trail.objects.get(pk=request.data["trail"])
        rating.user = request.auth.user
        rating.trail = trail
        rating.bathroom = request.data["bathroom"]
        rating.parking = request.data["parking"]
        rating.width = request.data["width"]
        rating.clear = request.data["clear"]
        rating.steep = request.data["steep"]

        rating.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        rating = Rating.objects.get(pk=pk)
        rating.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = Rating
        fields = ('id', 'user', 'trail', 'parking', 'bathroom', 'width', 'clear', 'steep')
