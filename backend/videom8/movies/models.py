# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblMovies(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    main_title = models.CharField(max_length=999)
    original_title = models.CharField(max_length=999)
    stripped_title = models.CharField(max_length=999)
    alternative_title = models.CharField(max_length=999)
    main_title_with_year = models.CharField(max_length=999)
    release_date = models.DateField(blank=True, null=True)
    release_year = models.IntegerField()
    link_to_the_movie = models.CharField(max_length=999, blank=True, null=True)
    high_qual_link_to_the_movie = models.CharField(max_length=999, blank=True, null=True)
    link_to_the_trailer = models.CharField(max_length=999, blank=True, null=True)
    movie_description = models.CharField(max_length=999, blank=True, null=True)
    imdb_site = models.CharField(max_length=999, blank=True, null=True)
    id_relationship = models.IntegerField(blank=True, null=True)
    based_on = models.CharField(max_length=999, blank=True, null=True)
    imdb_rating = models.FloatField(blank=True, null=True)
    roten_tomat_tomatometer = models.FloatField(blank=True, null=True)
    roten_tomat_audience_score = models.FloatField(blank=True, null=True)
    metacritic_meta_score = models.FloatField(blank=True, null=True)
    metacritic_user_score = models.FloatField(blank=True, null=True)
    filmweb_critics_score = models.FloatField(blank=True, null=True)
    filmweb_user_score = models.FloatField(blank=True, null=True)
    id_genres = models.IntegerField(blank=True, null=True)
    id_alternative_genres = models.IntegerField(blank=True, null=True)
    id_tags = models.IntegerField(blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'tbl_movies'

    def __str__(self):
        return self.main_title

# Unable to inspect table 'tbl_people'
# The error was: permission denied for table tbl_people
# Unable to inspect table 'tbl_roles'
# The error was: permission denied for table tbl_roles
# Unable to inspect table 'tbl_roles_relationship'
# The error was: permission denied for table tbl_roles_relationship
# Unable to inspect table 'tbl_title'
# The error was: permission denied for table tbl_title
