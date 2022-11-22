from django.urls import path
from .views import (MovieDetails, WatchList_APIView, Stream_APIView,
                    StreamPlatformDetails, ReviewList, ReviewDetail, ReviewCreate)
urlpatterns = [
    path('list/', WatchList_APIView.as_view(), name='Movies List'),
    path('<int:pk>', MovieDetails.as_view(), name='Movie Details'),
    path('stream/', Stream_APIView.as_view(), name='Stream List'),
    path('stream/<int:pk>', StreamPlatformDetails.as_view(),
         name='Stream Platform Details'),
    path('stream/<int:pk>/review/', ReviewDetail.as_view(),
         name='Review a certain movie'),
    path('stream/<int:pk>/review-create/', ReviewCreate.as_view(),
         name='Review a certain movie'),

    path('review/', ReviewList.as_view(), name='Stream Platform Details'),

]
