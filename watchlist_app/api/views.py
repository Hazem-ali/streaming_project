from watchlist_app.models import WatchList, StreamPlatform, Review
from rest_framework.response import Response
from .serializers import WatchListSerializer, StreamPlatformSerilizer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView


from rest_framework import generics




class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        serializer.save(watchlist=watchlist)
        # while saving, add watchlist value to watchlist variable


class ReviewList(generics.ListCreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # to customize query based on incoming request, override this function instead of using queryset
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)



class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class WatchList_APIView(APIView):
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


class Stream_APIView(APIView):
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
