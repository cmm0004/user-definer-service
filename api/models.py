from django.db import models

# Create your models here.
class TwitterUser(models.Model):
    """
    A TwitterUser is a follower that has had their Data collected
    classification
    0 - individual
    1 - business
    2 - blogger
    """
    user_id = models.IntegerField(primary_key = True)
    screen_name = models.CharField(max_length = 50)
    contributors_enabled = models.BooleanField()
    hours_since_last_tweet = models.IntegerField(null=True)
    declared_blogger = models.BooleanField()
    declared_company = models.BooleanField()
    num_entities = models.IntegerField()
    tweets_favorited = models.IntegerField()
    num_followers = models.IntegerField()
    num_friends = models.IntegerField()
    geo_enabled = models.BooleanField()
    is_translator = models.BooleanField()
    listed_count = models.IntegerField()
    protected = models.BooleanField()
    num_tweets = models.IntegerField()
    has_profile_url = models.BooleanField()
    verified = models.BooleanField()
    classification = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='api')

    def __str__(self):
        return self.screen_name + " - " + str(self.classification)

