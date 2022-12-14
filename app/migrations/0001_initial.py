# Generated by Django 4.0.1 on 2022-07-28 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=13, null=True)),
                ('last_name', models.CharField(blank=True, max_length=13, null=True)),
                ('mobileno', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_no', models.CharField(blank=True, max_length=13, null=True, unique=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
