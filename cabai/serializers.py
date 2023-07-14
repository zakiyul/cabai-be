from rest_framework import serializers
from . import models

class GejalaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GejalaModel
        fields = '__all__'

class PenyakitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PenyakitModel
        fields = '__all__'

class BasisPengetahuanSerializer(serializers.ModelSerializer):
    gejala = GejalaSerializer
    penyakit = PenyakitSerializer

    class Meta:
        model = models.BasisPengetahuan
        fields = '__all__'