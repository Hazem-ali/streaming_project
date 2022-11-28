from django.urls import path, include
from .views import (MovieDetails, WatchList_APIView, Stream_APIView,
                    StreamPlatformDetails, ReviewList, ReviewDetail, ReviewCreate, StreamPlatform_ViewSet)

from rest_framework.routers import DefaultRouter

router =DefaultRouter()

router.register('stream', StreamPlatform_ViewSet,'streamplatform')


urlpatterns = [
    path('list/', WatchList_APIView.as_view(), name='Movies List'),
    path('<int:pk>/', MovieDetails.as_view(), name='Movie Details'),

     path('', include(router.urls)),

#     path('stream/', Stream_APIView.as_view(), name='Stream List'),
#     path('stream/<int:pk>', StreamPlatformDetails.as_view(), name='Stream Platform Details'),
    
    path('stream/<int:pk>/reviews/', ReviewList.as_view(), name='Stream Platform Details'),
    path('<int:pk>/review/', ReviewDetail.as_view(), name='Get a review details'),
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name='Review a certain movie'),


]
