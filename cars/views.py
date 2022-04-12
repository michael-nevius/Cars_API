from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer
from .models import Car

@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        serilizer = CarSerializer(cars, many=True)   
        return Response(serilizer.data)

    elif request.method == 'POST':
        serilizer = CarSerializer(data=request.data)
        serilizer.is_valid(raise_exception=True)
        serilizer.save()
        return Response(serilizer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])    
def car_detail(request, pk):
    car = get_object_or_404(Car,pk=pk)
    if request.method == 'GET':
        serializer = CarSerializer(car);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerializer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    
       