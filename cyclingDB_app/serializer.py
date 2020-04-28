from rest_framework import serializers
from cyclingDB_app.models import *


class CyclistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cyclist
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class RaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Race
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SpecialtySerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialty
        fields = '__all__'


class TeamRaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRace
        fields = '__all__'


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stage
        fields = '__all__'