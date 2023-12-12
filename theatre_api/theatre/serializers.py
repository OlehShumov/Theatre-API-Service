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


class PlayListSerializer(PlaySerializer):
    actors = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="full_name")
    genres = serializers.SlugRelatedField(many=True,
                                          read_only=True,
                                          slug_field="name")

    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description",
                  "full_name",
                  "name")


class PlayDetailSerializer(PlaySerializer):
    actors = ActorSerializer(many=True)
    genres = GenreSerializer(many=True)
    performances = serializers.SlugRelatedField(many=True,
                                                read_only=True,
                                                slug_field="show_time")

    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description",
                  "duration",
                  "actors",
                  "genres",
                  "performances")


class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = ("id",
                  "play",
                  "theatre_hall",
                  "show_time")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id",
                  "row",
                  "seat",
                  "performance",
                  "reservation")

    def validate(self, attrs):
        data = super(TicketSerializer, self).validate(attrs=attrs)
        Ticket.validate_ticket(
            attrs["row"],
            attrs["seat"],
            attrs["performance"].theatre_hall,
        )
        return data


class ReservationSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True, allow_empty=False)

    class Meta:
        model = Reservation
        fields = ("id",
                  "created_at",
                  "tickets")

    @transaction.atomic
    def create(self, validated_data):
        with transaction.atomic():
            tickets_data = validated_data.pop('tickets')
            reservation = Reservation.objects.create(**validated_data)
            for ticket_data in tickets_data:
                Ticket.objects.create(reservation=reservation, **ticket_data)
        return reservation


class PerformanceListSerializer(PerformanceSerializer):
    play = PlaySerializer()
    theatre_hall = TheatreHallSerializer()

    class Meta:
        model = Performance
        fields = ("id",
                  "play",
                  "theatre_hall",
                  "show_time")


class PerformanceDetailSerializer(PerformanceSerializer):
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


class PlayListSerializer(PlaySerializer):
    class Meta:
        model = Play
        fields = ("id",
                  "title",
                  "description")


class PlayDetailSerializer(PlaySerializer):
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


class TheatreHallListSerializer(TheatreHallSerializer):
    class Meta:
        model = TheatreHall
        fields = ("id",
                  "name",
                  "rows",
                  "seats_in_row")


class TheatreHallDetailSerializer(TheatreHallSerializer):
    performances = PerformanceListSerializer(many=True)

    class Meta:
        model = TheatreHall
        fields = ("id",
                  "name",
                  "rows",
                  "seats_in_row",
                  "performances")


class GenreListSerializer(GenreSerializer):
    class Meta:
        model = Genre
        fields = ("id",
                  "name")


class ActorListSerializer(ActorSerializer):
    class Meta:
        model = Actor
        fields = ("id",
                  "first_name",
                  "last_name")


class TicketListSerializer(TicketSerializer):
    pass


class ReservationListSerializer(ReservationSerializer):
    class Meta:
        model = Reservation
        fields = ("id",
                  "created_at",
                  "user")
