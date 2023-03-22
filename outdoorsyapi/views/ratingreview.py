"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from outdoorsyapi.models import RatingReview, Rating, Review


class RatingReviewView(ViewSet):
    
    def retrieve(self, request, pk):
        ratingreview = RatingReview.objects.get(pk=pk)
        serializer = RatingReviewSerializer(ratingreview)
        return Response(serializer.data)
       
            


    def list(self, request):
        ratingreviews = RatingReview.objects.all()
        serializer = RatingReviewSerializer(ratingreviews, many=True)
        return Response(serializer.data)
    
    def create(self, request):

        rating = Rating.objects.get(pk=request.data["rating"])
        review = Review.objects.get(pk=request.data["review"])

        ratingreview = RatingReview.objects.create(
            rating= rating,
            review= review
            )
        serializer = RatingReviewSerializer(ratingreview)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        ratingreview = RatingReview.objects.get(pk=pk)
        ratingreview.rating = Rating.objects.get(pk=request.data["rating"])
        ratingreview.review = Review.objects.get(pk=request.data["review"])

        ratingreview.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        ratingreview = RatingReview.objects.get(pk=pk)
        ratingreview.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class RatingReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for trails
    """
    class Meta:
        model = RatingReview
        fields = ('id','rating', 'review')
