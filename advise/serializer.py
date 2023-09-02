from rest_framework import serializers

class DataScoreSerializer(serializers.Serializer):
    ID = serializers.CharField()
    UNIVESITY = serializers.CharField()
    URL = serializers.CharField()
    CODE = serializers.CharField()
    NAME = serializers.CharField()
    SCORE = serializers.FloatField()
    METHOD = serializers.CharField()