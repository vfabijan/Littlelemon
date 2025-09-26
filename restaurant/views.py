from django.shortcuts import render
from django.http import HttpResponse 
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer

# Create your views here.

def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]