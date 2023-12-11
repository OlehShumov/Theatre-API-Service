from django.db import models

from django.conf import settings


class TheatreHall(models.Model):
    name = models.CharField(max_length=63)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=63)

    def __str__(self):
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)

    def __str__(self):
        return (f"{self.first_name}, "
                f"{self.last_name}")


class Play(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.DO_NOTHING)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.DO_NOTHING)
    show_time = models.DateTimeField()

    def __str__(self):
        return (f"{self.play}, "
                f"{self.theatre_hall.name}, "
                f"{self.show_time}")


class User(AbstractUser):
    pass


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MOODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return (f"{self.user}, "
                f"{self.created_at}")


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.DO_NOTHING)
    reservation = models.ForeignKey(Reservation, on_delete=models.DO_NOTHING)

    def __str__(self):
        return (f"{self.row}, "
                f"{self.seat}, "
                f"{self.performance}, "
                f"{self.reservation}")
