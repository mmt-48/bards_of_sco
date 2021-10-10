from django.db import models
from django.urls import reverse


class Composer(models.Model):
    name_composer = models.CharField(max_length=200, db_index=True)
    fam_composer = models.CharField(max_length=200, db_index=True, default='')
    photo = models.ImageField(upload_to='composer', default='')
    orderr = models.CharField(max_length=3, default='',blank=True, null=True)
    background_ph = models.ImageField(upload_to='composer', default='',blank=True, null=True)
    sco = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name_composer+self.fam_composer

    class Meta:
        verbose_name = 'composer'
        verbose_name_plural = 'composers'

    def get_absolute_url(self):
        return reverse('index', kwargs={'comp_id': self.pk})


class Avtor_text(models.Model):
    name_avtor_text = models.CharField(max_length=200, db_index=True)
    fam_avtor_text = models.CharField(max_length=200, db_index=True, default='')
    photo = models.ImageField(upload_to='avtor', default='')

    def __str__(self):
        return self.name_avtor_text+self.fam_avtor_text

    class Meta:
        verbose_name = 'avtor_text'
        verbose_name_plural = 'avtors_text'

    def get_absolute_url(self):
        return reverse('Avtor_text', kwargs={'comp_id': self.pk})


class Translator(models.Model):
    name_translator = models.CharField(max_length=200, db_index=True)
    fam_translator = models.CharField(max_length=200, db_index=True, default='')
    photo = models.ImageField(upload_to='translator', default='')

    def __str__(self):
        return self.fam_translator

    class Meta:
        verbose_name = 'translator'
        verbose_name_plural = 'translators'

    def get_absolute_url(self):
        return reverse('Translator', kwargs={'art_id': self.pk})


class Artist(models.Model):
    name_artist = models.CharField(max_length=200, db_index=True)
    fam_artist = models.CharField(max_length=200, db_index=True, default='')
    photo = models.ImageField(upload_to='artist', default='')
    sco = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name_artist+self.fam_artist

    class Meta:
        verbose_name = 'artist'
        verbose_name_plural = 'artists'

    def get_absolute_url(self):
        return reverse('artist', kwargs={'art_id': self.pk})


class Song(models.Model):
    comp_id = models.ForeignKey('composer', on_delete=models.PROTECT, null=True, db_index=True)
    comp1_id = models.ForeignKey('composer1', on_delete=models.PROTECT, blank=True, null=True, db_index=True)
    avt_id = models.ForeignKey('avtor_text', on_delete=models.PROTECT, null=True, db_index=True)
    trans_id = models.ForeignKey('translator', on_delete=models.PROTECT, blank=True, null=True, db_index=True)
    name_song = models.CharField(max_length=200, db_index=True)
    workfield = models.IntegerField(blank=True, null=True, default=0)
    language = models.CharField(max_length=20, default='', blank=True, null=True)

    def __str__(self):
        return self.name_song

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'

    def get_absolute_url(self):
        return reverse('song', kwargs={'song_id': self.pk})


class Execution(models.Model):
    song_id = models.ForeignKey('song', on_delete=models.PROTECT, null=True, db_index=True)
    artist_id = models.ForeignKey('artist', on_delete=models.PROTECT, null=True, db_index=True)
    audio_file = models.FileField(upload_to='audio/')
    note = models.CharField(max_length=200, db_index=True)
    workfield = models.CharField(max_length=200, db_index=True, blank=True)
    workfield1 = models.IntegerField(blank=True, null=True)
    workfield2 = models.IntegerField(blank=True, null=True)
    workfield3 = models.IntegerField(blank=True, null=True)
    sco = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.note

    class Meta:
        verbose_name = 'execution'
        verbose_name_plural = 'executions'

    def get_absolute_url(self):
        return reverse('index02', kwargs={'exec_id': self.pk})


class Composer1(models.Model):
    name_composer = models.CharField(max_length=200, db_index=True)
    fam_composer = models.CharField(max_length=200, db_index=True, default='')
    photo = models.ImageField(upload_to='composer', default='')
    fon = models.ImageField(upload_to='composer', default='')
    fon1 = models.ImageField(upload_to='composer', default='')

    def __str__(self):
        return self.fam_composer

    class Meta:
        verbose_name = 'composer1'
        verbose_name_plural = 'composer1s'

    def get_absolute_url(self):
        return reverse('composer1', kwargs={'comp1_id': self.pk})


class Cvisit(models.Model):
    count_visit = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.count_visit)

    class Meta:
        verbose_name = 'cvisit'
        verbose_name_plural = 'cvisits'
