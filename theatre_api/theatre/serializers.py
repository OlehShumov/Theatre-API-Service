from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import (
    Performance,
    Play,
    TheatreHall,
    Genre,
    Actor,
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

    def validate(self, attrs):
        performance = attrs.get("performance")
        row = attrs.get("row")
        seat = attrs.get("seat")
        reservation = attrs.get("reservation")
        if Ticket.objects.filter(performance=performance, row=row, seat=seat).exists():
            raise ValidationError("This seat is already taken")
        if reservation and reservation.performance != performance:
            raise ValidationError("Reservation and performance should be the same")
        return attrs


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


class TheatreHallListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id",
                  "name",
                  "rows",
                  "seats_in_row")


class TheatreHallDetailSerializer(serializers.ModelSerializer):
    performances = PerformanceListSerializer(many=True)

    class Meta:
        model = TheatreHall
        fields = ("id",
                  "name",
                  "rows",
                  "seats_in_row",
                  "performances")


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ("id",
                  "name")


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id",
                  "first_name",
                  "last_name")

