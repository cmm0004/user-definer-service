from rest_framework import serializers
from api.models import TwitterUser


class TwitterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterUser
        fields = ('user_id',
                    'screen_name',
                    'contributors_enabled',
                    'hours_since_last_tweet',
                    'declared_blogger',
                    'declared_company',
                    'num_entities',
                    'tweets_favorited',
                    'num_followers',
                    'num_friends',
                    'geo_enabled',
                    'is_translator',
                    'listed_count',
                    'protected' ,
                    'num_tweets',
                    'has_profile_url',
                    'verified',
                    'classification',
                )