from django.shortcuts import render
from django.http import HttpResponse, response

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import models
from . import serializers

@api_view(['GET', 'POST'])
def gejala_list(request):
    if request.method == 'GET':
        gejala = models.GejalaModel.objects.all()
        serializer = serializers.GejalaSerializer(gejala, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.GejalaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def penyakit_list(request):
    if request.method == 'GET':
        penyakit = models.PenyakitModel.objects.all()
        serializer = serializers.PenyakitSerializer(penyakit, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.PenyakitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'POST'])
def basispengetahuan_list(request):
    if request.method == 'GET':
        basispengetahuan = models.BasisPengetahuan.objects.all()
        serializer = serializers.BasisPengetahuanSerializer(basispengetahuan, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = serializers.BasisPengetahuanSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    