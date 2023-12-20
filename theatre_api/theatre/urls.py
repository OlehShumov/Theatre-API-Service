from django.urls import path, include
from rest_framework import routers

from theatre.views import (
    PerformanceViewSet,
    ActorViewSet,
    TheatreHallViewSet,
    GenreViewSet,
    PlayViewSet,
    TicketViewSet,
    ReservationViewSet,
)


router = routers.DefaultRouter()
router.register("performances", PerformanceViewSet)
router.register("actors", ActorViewSet)
router.register("theatres", TheatreHallViewSet)
router.register("genres", GenreViewSet)
router.register("plays", PlayViewSet)
router.register("tickets", TicketViewSet)
router.register("reservations", ReservationViewSet)


urlpatterns = [path("", include(router.urls))]

app_name = "theatre"
