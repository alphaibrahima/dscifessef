# Generated by Django 3.0.5 on 2020-04-14 06:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateurs', '0002_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('description', models.TextField(blank=True, max_length=500)),
                ('phone_number', models.CharField(blank=True, max_length=12)),
                ('club_name', models.CharField(blank=True, max_length=50)),
                ('address', models.TextField(blank=True, max_length=500)),
                ('date', models.DateField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='profile_default.jpg', null=True, upload_to='users_profile/')),
            ],
        ),
    ]