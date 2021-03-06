# Generated by Django 3.2.7 on 2021-10-20 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abirvab', '0002_auto_20211020_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoiBahar',
            fields=[
                ('boiBaharId', models.IntegerField(primary_key=True, serialize=False)),
                ('boiBaharText', models.TextField()),
                ('boiBaharFile', models.FileField(upload_to='books')),
                ('authorFirstName', models.CharField(max_length=15)),
                ('authorLastName', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('otherId', models.IntegerField(primary_key=True, serialize=False)),
                ('otherText', models.TextField()),
                ('otherFile', models.FileField(upload_to='others')),
                ('authorFirstName', models.CharField(max_length=15)),
                ('authorLastName', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Probondho',
            fields=[
                ('probondhoId', models.IntegerField(primary_key=True, serialize=False)),
                ('probondhoText', models.TextField()),
                ('authorFirstName', models.CharField(max_length=15)),
                ('authorLastName', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='boireview',
            name='boiReviewFile',
            field=models.FileField(upload_to='boi reviews'),
        ),
        migrations.AlterField(
            model_name='cinemareview',
            name='cinemaReviewFile',
            field=models.FileField(upload_to='cinema reviews'),
        ),
        migrations.AlterField(
            model_name='rannabanna',
            name='rannaBannaFile',
            field=models.FileField(upload_to='ranna bannas'),
        ),
    ]
