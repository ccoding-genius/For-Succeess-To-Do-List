# Generated by Django 2.0 on 2022-06-11 11:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('memo', models.TextField()),
                ('pin_money', models.IntegerField(default=500)),
                ('is_completed', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
