# Generated by Django 5.0.6 on 2024-07-25 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_boat_remove_bookings_boat_id_remove_tariffs_boat_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariff',
            name='days_amount',
            field=models.CharField(choices=[(3, '3 Дня'), (5, '5 Дней'), (7, '7 Дней')], help_text='количество дней тарифа', max_length=20),
        ),
    ]
