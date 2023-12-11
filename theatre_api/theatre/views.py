from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .models import (
    Performance,
    Play,
    TheatreHall,
    Genre,
    Actor,
    Ticket,
    Reservation,
)
from .serializers import (
    PerformanceSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    GenreSerializer,
    ActorSerializer,
    TicketSerializer,
    ReservationSerializer,
)


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class TheatreHallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PlayViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class PerformanceViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class TicketViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Ticket.objects.prefetch_related("reservation", "performance")
    serializer_class = TicketSerializer


class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

