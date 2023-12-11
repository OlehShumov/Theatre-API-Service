from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Performance,
    Play,
    Genre,
    Actor,
    TheatreHall,
    Ticket,
    Reservation,
)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id", "name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id",
                  "name",
                  "rows",
                  "seats_in_row")


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id",
                  "row",
                  "seat",
                  "performance",
                  "reservation")


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ("id",
                  "created_at",
                  "user")


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id",
                  "play",
                  "theatre_hall",
                  "show_time")


class PerformanceListSerializer(serializers.ModelSerializer):
    play = PlaySerializer()
    theatre_hall = TheatreHallSerializer()

    class Meta:
        model = Performance
        fields = ("id",
                  "play",
                  "theatre_hall",
                  "show_time")


class PerformanceDetailSerializer(serializers.ModelSerializer):
    play = PlaySerializer()
    theatre_hall = TheatreHallSerializer()
    tickets = TicketSerializer(many=True)

    class Meta:
        model = Performance
        fields = ("id",
                  "play",
                  "theatre_hall",
                  "show_time",
                  "tickets")


class PlayListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description")


class PlayDetailSerializer(serializers.ModelSerializer):
    performances = PerformanceListSerializer(many=True)
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)

    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description",
                  "performances",
                  "actors",
                  "genres")

