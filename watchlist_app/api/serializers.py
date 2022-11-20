from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform




class WatchListSerializer(serializers.ModelSerializer):


    class Meta:
        model = WatchList
        # Control Data Display 
        fields = '__all__'
        # exclude = ['id']



class StreamPlatformSerilizer(serializers.ModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        # Control Data Display 
        fields = '__all__'
        # exclude = ['id']



