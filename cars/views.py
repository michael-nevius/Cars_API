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
@api_view(['GET'])    
def car_detail(request, pk):
    try:
        car = Car.objects.get(pk=pk)
        serializer = CarSerializer(car);
        return Response(serializer.data)
    except Car.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
       