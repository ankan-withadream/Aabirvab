# Generated by Django 3.2.7 on 2021-10-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kobita',
            fields=[
                ('kobitaId', models.IntegerField(primary_key=True, serialize=False)),
                ('contentId', models.IntegerField()),
                ('kobitaText', models.TextField()),
                ('authorFirstName', models.CharField(max_length=50)),
                ('authorLastName', models.CharField(max_length=50)),
            ],
        ),
    ]
