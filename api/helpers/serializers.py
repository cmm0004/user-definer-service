from rest_framework import serializers
from api.models import TwitterUser
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    twitterusers = serializers.PrimaryKeyRelatedField(many=True, queryset=TwitterUser.objects.all())

    class Meta:
            model = User
            fields = ('id', 'username', 'twitterusers')

class TwitterUserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
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
                    'owner'
                )
        