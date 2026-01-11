from django.http import JsonResponse
from django.views import View
from django.db.models import Avg

from .models import ReviewModel


class ReviewView(View):

    def get(self, request):
        # fetch all reviews (newest first)
        reviews = ReviewModel.objects.all().order_by('-createdAt')

        reviews_list = []
        for review in reviews:
            reviews_list.append({
                "id": review.id,
                "name": review.name,
                "rating": review.rating,
                "comment": review.comment,
                "createdAt": review.createdAt
            })

        # calculate average rating
        average_rating = reviews.aggregate(avg=Avg('rating'))['avg']
        average_rating = int(average_rating) if average_rating else 0

        return JsonResponse({
            "average": average_rating,
            "totalReviews": reviews.count(),
            "reviews": reviews_list
        })

    def post(self, request):
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        if not name or not rating:
            return JsonResponse(
                {"message": "Name and rating are required"},
                status=400
            )

        review = ReviewModel.objects.create(
            name=name,
            rating=rating,
            comment=comment
        )

        return JsonResponse({
            "message": "Review added successfully",
            "review": {
                "id": review.id,
                "name": review.name,
                "rating": review.rating,
                "comment": review.comment
            }
        }, status=201)
