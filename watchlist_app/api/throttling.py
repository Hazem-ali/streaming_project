from rest_framework.throttling import AnonRateThrottle, UserRateThrottle


class StreamPlatformThrottle(UserRateThrottle):
    scope = 'stream-platform'
    
