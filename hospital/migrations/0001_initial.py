# Generated by Django 4.1.12 on 2023-10-28 11:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospital_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_email', models.EmailField(max_length=200)),
                ('hospital_phone', models.BigIntegerField()),
                ('hospital_owner_name', models.CharField(max_length=200)),
                ('hospital_owner_phone', models.BigIntegerField()),
                ('hospital_owner_email', models.EmailField(max_length=200)),
                ('hospital_address', models.CharField(max_length=200)),
                ('hospital_city', models.CharField(max_length=200)),
                ('hospital_status', models.BooleanField()),
                ('hospital_logo', models.ImageField(upload_to='hospital_logo/')),
                ('hospital_type', models.CharField(max_length=200)),
                ('hospital_category', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]