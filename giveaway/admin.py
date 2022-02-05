# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Competitor, Article, DayPassResort, GiveAway, GiveAwayWinner


@admin.register(Competitor)
class CompetitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'ig_username', 'name', 'email')
    search_fields = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'model', 'description', 'value')
    search_fields = ('name',)


@admin.register(DayPassResort)
class DayPassResortAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'resort', 'description', 'address', 'date')
    list_filter = ('date',)
    search_fields = ('name',)


@admin.register(GiveAway)
class GiveAwayAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'date', 'number_of_winners')
    list_filter = ('date',)
    search_fields = ('name',)


@admin.register(GiveAwayWinner)
class GiveAwayWinnerAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'competitor',
        'giveaway',
        'content_type',
        'object_id',
    )
    list_filter = ('competitor', 'giveaway', 'content_type')