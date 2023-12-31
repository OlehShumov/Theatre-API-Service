from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.viewsets import GenericViewSet
from drf_spectacular.utils import extend_schema
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes
from rest_framework.pagination import PageNumberPagination

from .permissions import IsAdminOrIfAuthenticatedReadOnly
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
    PlayListSerializer,
    PlayDetailSerializer,
    PerformanceListSerializer,
    PerformanceDetailSerializer,
)


class GenreViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class TheatreHallViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class PlayViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Play.objects.prefetch_related("actors", "genres")
    serializer_class = PlaySerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    @staticmethod
    def _param_to_int(qs):
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self):
        genres = self.request.query_params.get("genres")
        actors = self.request.query_params.get("actors")
        queryset = self.queryset
        if genres:
            genre_ids = self._param_to_int(genres)
            queryset = queryset.filter(genres__id__in=genre_ids)
        if actors:
            actor_ids = self._param_to_int(actors)
            queryset = queryset.filter(actors__id__in=actor_ids)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        elif self.action == "retrieve":
            return PlayDetailSerializer
        return PlaySerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.select_related("play",
                                                  "theatre_hall")
    serializer_class = PerformanceSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)

    def get_queryset(self):
        queryset = self.queryset
        date = self.request.query_params.get("date")
        if date:

            queryset = queryset.filter(show_time__date=date)
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PerformanceListSerializer
        elif self.action == "retrieve":
            return PerformanceDetailSerializer
        return PerformanceSerializer

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="date",
                description="Filter performances by date",
                required=False,
                type=OpenApiTypes.DATE,
            ),
        ],
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class TicketViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Ticket.objects.prefetch_related("reservation", "performance")
    serializer_class = TicketSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)


class ReservationPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 100


class ReservationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    pagination_class = ReservationPagination
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly,)
