from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework.response import Response
from .serializers import WatchListSerializer, StreamPlatformSerilizer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView

from rest_framework.exceptions import ValidationError
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsReviewUserOrReadOnly, IsAdminOrReadOnly

from .throttling import StreamPlatformThrottle

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .pagination import ReviewsPagination


class UserReviewList(generics.ListCreateAPIView):

    serializer_class = ReviewSerializer
    # to customize query based on incoming request, override this function instead of using queryset
    

    def get_queryset(self):
        username = self.kwargs['username']
        return Review.objects.filter(review_user__username=username)


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):

        return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')  # pk of the watchlist (passed in the url)
        watchlist = WatchList.objects.get(pk=pk)

        # getting the user from request and searching for a review for this user
        # search is performed with foreign keys assigned
        review_user = self.request.user
        review_queryset = Review.objects.filter(
            watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError('Already reviewed this movie!')
        else:
            # Adding rating logic into watchlist
            if watchlist.avg_rating == 0:
                watchlist.avg_rating = serializer.validated_data['rating']
            else:
                watchlist.avg_rating = (
                    watchlist.avg_rating + serializer.validated_data['rating']) / 2
            watchlist.num_ratings += 1

        watchlist.save()
        serializer.save(watchlist=watchlist, review_user=review_user)
        # while saving, add watchlist value to watchlist variable


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['review_user__username','rating']

    pagination_class = ReviewsPagination

    # to customize query based on incoming request, override this function instead of using queryset
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewUserOrReadOnly]


class WatchList_APIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        WatchLists = WatchList.objects.all()

        serializer = WatchListSerializer(WatchLists, many=True)

        return Response(serializer.data)

    def post(self, request):

        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class MovieDetails(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)

        except WatchList.DoesNotExist:
            return Response({'error': 'WatchList not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)

        return Response(serializer.data)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)

        serializer = WatchListSerializer(movie, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatform_ViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]

    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerilizer
    throttle_classes = [StreamPlatformThrottle]


# class StreamPlatform_ViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerilizer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerilizer(user)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = StreamPlatformSerilizer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


class Stream_APIView(APIView):
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request):
        streams = StreamPlatform.objects.all()
        serializer = StreamPlatformSerilizer(streams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerilizer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class StreamPlatformDetails(APIView):

    def get(self, request, pk):
        try:
            stream = StreamPlatform.objects.get(pk=pk)

        except StreamPlatform.DoesNotExist:
            return Response({'error': 'Stream not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = StreamPlatformSerilizer(stream)

        return Response(serializer.data)

    def put(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)

        serializer = StreamPlatformSerilizer(stream, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

    def delete(self, request, pk):
        stream = StreamPlatform.objects.get(pk=pk)
        stream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
