from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from datetime import datetime

from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer, BookingDetailsSerializer, UpdateBookingSerializer, RegisterSerializer



class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer


	def get_queryset(self):
		return Booking.objects.filter(user=self.request.user)



class BooingsListUpdateAdmin(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer

	def get_serializer_class(self):
		assert self.serializer_class is not None, (
			"'%s' should either include a `serializer_class` attribute, "
			"or override the `get_serializer_class()` method."
			% self.__class__.__name__
		)

		return self.serializer_class





class BookingDetails(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = BookingDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class UpdateBooking(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateBookingSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'


class CancelBooking(DestroyAPIView):
	queryset = Booking.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'



# booking create view 
class BookFlight(CreateAPIView):
	serializer_class = UpdateBookingSerializer

	def perform_create(self, serializer):
		serializer.save(user=self.request.user, flight_id=self.kwargs['flight_id'])


class Register(CreateAPIView):
	serializer_class = RegisterSerializer
