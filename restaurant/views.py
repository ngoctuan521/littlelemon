from django.shortcuts import render
import rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
import rest_framework.viewsets


from .serializer import ModelSerializer, BookingSerializer
from .models import Booking, Menu


# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    """
    API endpoint that allows menu items to be viewed or created.
    """
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    permission_classes = [IsAuthenticated]
    # def get_queryset(self):
        # return Menu.objects.all().filter(user=self.request.user)
        


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a single menu item to be viewed, edited or deleted.
    """
    queryset = Menu.objects.all()
    serializer_class = ModelSerializer
    # permission_classes = [IsAuthenticated]
    # lookup_field = 'id'  # Use id as the lookup field

    # def get_object(self):
    #     """Override to get the user by username."""
    #     id = self.kwargs.get('id')
    #     return Menu.objects.get(id=id)

class BookingViewSet(generics.ListCreateAPIView):
    """
    API endpoint that allows bookings to be viewed or created.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # permission_classes = [IsAuthenticated]


