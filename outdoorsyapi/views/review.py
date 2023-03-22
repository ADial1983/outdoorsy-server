"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import Review, Trail


class ReviewView(ViewSet):
    
    def retrieve(self, request, pk):
        review = Review.objects.get(pk=pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)
       
            


    def list(self, request):
        if "trail" in request.query_params:
            reviews = Review.objects.filter(trail_id=request.query_params['trail'])
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
        else: 
            reviews = Review.objects.all()
            serializer = ReviewSerializer(reviews, many=True)
            return Response(serializer.data)
    

    def create(self, request):

        trail = Trail.objects.get(pk=request.data["trail"])

        review = Review.objects.create(
            user= request.auth.user,
            trail= trail,
            review = request.data["review"]
            )
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        review = Review.objects.get(pk=pk)
        trail = Trail.objects.get(pk=request.data["trail"])
        review.user = request.auth.user
        review.trail = trail
        review.review = request.data["review"]

        review.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        review = Review.objects.get(pk=pk)
        review.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = Review
        fields = ('id','user', 'trail', 'review')
