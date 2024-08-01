import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# from rest_framework import serializers


class Boat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    boat_name = models.CharField(max_length=100, blank=False, null=False, help_text="имя лодки")
    boat_capacity = models.IntegerField(blank=False, null=False)
    current_load = models.IntegerField(blank=False, null=False)
    status = models.CharField(max_length=50, blank=False, null=False, help_text="статус")

    def __str__(self):
        return self.boat_name


class Tariff(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    boat = models.ForeignKey(Boat, on_delete=models.PROTECT, help_text="id лодки")

    FIRST = 3
    SECOND = 5
    THIRD = 7
    DAYS_AMOUNTS = [
        (FIRST, '3 Дня'),
        (SECOND, '5 Дней'),
        (THIRD, '7 Дней'),
    ]
    days_amount = models.CharField(max_length=20, choices=DAYS_AMOUNTS, blank=False, help_text='количество дней тарифа')
    price = models.DecimalField(max_digits=20, decimal_places=2, blank=False, null=False, help_text="стоимость билета")

    def __str__(self):
        return f'{self.get_days_amount_display()} - {self.price}'


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creating_date = models.DateTimeField(auto_now_add=True, editable=False, help_text="дата создания")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    boat = models.ForeignKey(Boat, on_delete=models.PROTECT, help_text="id лодки")
    tariff = models.ForeignKey(Tariff, on_delete=models.PROTECT, help_text="id тарифа")
    tickets_amount = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=1,
        # validators=[
        #     MinValueValidator(1),
        #     MaxValueValidator(self.seats_amount)
        # ]
    )

    first_date = models.DateTimeField(help_text="начало путешествия")
    last_date = models.DateTimeField(help_text="конец путешествия")
    status = models.CharField(null=True, max_length=50, help_text="статус")

    def seats_amount(self):
        b_id = Boat.objects.get(self.boat)
        return ()

    # class MultipleOf:
    #     def __init__(self, base):
    #         self.base = base
    #
    #     def __call__(self, value):
    #         if value % self.base != 0:
    #             message = 'This field must be a multiple of %d.' % self.base
    #             raise serializers.ValidationError(message)
    #

    def __str__(self):
        return f'{self.user.username if self.user else "Unknown"} - {self.boat.boat_name} - {self.status}'


class Notification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(max_length=50, null=False, blank=False, help_text="тип уведомления")
    message = models.CharField(max_length=250, null=False, blank=False, help_text="текст уведомления")
    user = models.ForeignKey(User, on_delete=models.PROTECT, help_text="id пользователя")

    def __str__(self):
        return self.message


class Page(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


























# import uuid
# import django.contrib.auth.models
# from django.db import models
# from django.contrib.auth.models import User
#
#
# class Boats(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     boat_name = models.CharField(
#         max_length=100,
#         blank=False,
#         null=False,
#         help_text="имя лодки",
#     )
#     boat_capacity = models.IntegerField(
#         blank=False,
#         null=False,
#     )
#     current_load = models.IntegerField(
#         blank=False,
#         null=False,
#     )
#     status = models.CharField(
#         max_length=50,
#         blank=False,
#         null=False,
#         help_text="статус",
#     )
#
#     def __str__(self):
#         return self.boat_name
#
#
# class Tariffs(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     boat_id = models.ForeignKey(
#         to="Boats",
#         on_delete=models.PROTECT,
#         help_text="id лодки"
#     )
#
#     FIRST = '3D'
#     SECOND = '5D'
#     THIRD = '7D'
#     DAYS_AMOUNTS = [
#         (FIRST, '3 Дня'),
#         (SECOND, '5 Дней'),
#         (THIRD, '7 Дней'),
#     ]
#     days_amount = models.CharField(
#         max_length=20,
#         choices=DAYS_AMOUNTS,
#         blank=False,
#         help_text='количество дней тарифа'
#     )
#
#     price = models.DecimalField(
#         max_digits=20,
#         decimal_places=2,
#         blank=False,
#         null=False,
#         help_text="стоимость билета"
#     )
#
#     def __str__(self):
#         return f'{self.get_days_amount_display()} - {self.boat_id} - {self.price}'
#
#
# class Bookings(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#     )
#     creating_date = models.DateTimeField(
#         auto_now_add=True,
#         editable=False,
#         help_text="дата создания",
#     )
#
#     user_id = models.ForeignKey(
#         to=User,
#         on_delete=models.SET_NULL,
#         null=True,
#         blank=True,
#     )
#     boat_id = models.ForeignKey(
#         to="Boats",
#         on_delete=models.PROTECT,
#         help_text="id лодки",
#     )
#     tariff_id = models.ForeignKey(
#         to="Tariffs",
#         on_delete=models.PROTECT,
#         help_text="id тарифа",
#     )
#     tickets_amount = models.PositiveIntegerField(
#         blank=False,
#         null=False,
#         default=1,
#     )
#     first_date = models.DateTimeField(
#         help_text="начало путешествия",
#     )
#     last_date = models.DateTimeField(
#         help_text="конец путешествия",
#     )
#     status = models.CharField(
#         null=True,
#         max_length=50,
#         help_text="статус",
#     )
#
#     def __str__(self):
#         return f'{self.user.username if self.user else "Unknown"} - {self.boat.boat_name} - {self.status}'
#
# class Notifications(models.Model):
#     id = models.UUIDField(
#         primary_key=True,
#         default=uuid.uuid4,
#     )
#     type = models.CharField(
#         max_length=50,
#         null=False,
#         blank=False,
#         help_text="тип уведомления",
#     )
#     message = models.CharField(
#         max_length=250,
#         null=False,
#         blank=False,
#         help_text="текст уведомления",
#     )
#     manager_id = models.ForeignKey(
#         to=User,
#         on_delete=models.PROTECT,
#         help_text="id менеджера",
#     )
#
#     def __str__(self):
#         return self.message
#
#
# class Page(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.title
