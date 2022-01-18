# Generated by Django 3.2.5 on 2022-01-17 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('blood_group', models.CharField(max_length=10)),
                ('attender_name', models.CharField(max_length=50)),
                ('quantity', models.CharField(max_length=30)),
                ('hosiptal', models.CharField(max_length=70)),
                ('deadline', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('pincode', models.CharField(max_length=20)),
            ],
        ),
    ]
