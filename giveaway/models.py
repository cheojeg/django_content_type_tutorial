from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
import gfklookupwidget.fields as gfklookup_fields


class Competitor(models.Model):

    ig_username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    class Meta:

        verbose_name = 'Competitor'
        verbose_name_plural = 'Competitors'

    def __str__(self):
        return f'{self.ig_username}'


class Article(models.Model):

    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField()
    value = models.FloatField()

    class Meta:

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return f'{self.id} - {self.name}'


class DayPassResort(models.Model):

    name = models.CharField(max_length=100)
    resort = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    date = models.DateField()

    class Meta:

        verbose_name = 'Day Pass Resort'
        verbose_name_plural = 'Day Pass Resort'

    def __str__(self):
        return f'{self.id} - {self.resort}'


class GiveAway(models.Model):

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateField()
    number_of_winners = models.PositiveIntegerField()

    class Meta:

        verbose_name = 'GiveAway'
        verbose_name_plural = 'GiveAway'

    def __str__(self):
        return f'{self.name}'


class GiveAwayWinner(models.Model):

    competitor = models.ForeignKey(Competitor, on_delete=models.CASCADE)
    giveaway = models.ForeignKey(GiveAway, on_delete=models.CASCADE)
    limit = models.Q(app_label='giveaway', model='article') | \
        models.Q(app_label='giveaway', model='daypassresort')    
    content_type = models.ForeignKey(ContentType,  limit_choices_to=limit, on_delete=models.CASCADE)
    object_id = gfklookup_fields.GfkLookupField('content_type')
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:

        verbose_name = 'GiveAway Winner'
        verbose_name_plural = 'GiveAway Winner'

    def __str__(self):
        return f'{self.id} - {self.competitor.name} - {self.content_type} - {self.id}'