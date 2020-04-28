from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=70, blank=False)
    objects = models.Manager()
    
    def _str_(self):
        return "%s" % self.name


class Team(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=70, blank=False)
    manager = models.CharField(max_length=70, blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.name


class Race(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=70, blank=False)
    popularity = models.IntegerField(blank=False)
    num_stages = models.IntegerField(blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.name


class TeamRace(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    race = models.ForeignKey(Race, on_delete=models.CASCADE, blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.team.name


class Specialty(models.Model):
    name = models.CharField(max_length=70, blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.name


class Stage(models.Model):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, blank=False)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=70, blank=False)
    day = models.IntegerField(blank=False)
    month = models.IntegerField(blank=False)
    stage_number = models.IntegerField(blank=False)
    stage_km = models.IntegerField(blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.name


class Cyclist(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=False)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, blank=False)
    lastname = models.TextField(blank=False)
    firstname = models.TextField(blank=False)
    birthdate = models.DateField(blank=False)
    popularity = models.IntegerField(blank=False)
    leader = models.BooleanField(blank=False)
    size = models.FloatField(blank=False)
    weight = models.FloatField(blank=False)
    mountain = models.IntegerField(blank=False)
    plain = models.IntegerField(blank=False)
    downhilling = models.IntegerField(blank=False)
    sprint = models.IntegerField(blank=False)
    resistance = models.IntegerField(blank=False)
    recuperation = models.IntegerField(blank=False)
    timetrial = models.IntegerField(blank=False)
    objects = models.Manager()

    def _str_(self):
        return "%s" % self.firstname
