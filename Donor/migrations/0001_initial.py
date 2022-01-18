# Generated by Django 3.2.5 on 2022-01-18 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('donor_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10, null=True)),
                ('gender', models.CharField(max_length=30, null=True)),
                ('age', models.BinaryField(null=True)),
                ('blood_group', models.CharField(max_length=30, null=True)),
                ('lat_lon', models.CharField(max_length=200)),
                ('pincode', models.BinaryField()),
                ('contact_method', models.CharField(blank=True, max_length=100, null=True)),
                ('whatsapp_no', models.CharField(max_length=30, null=True)),
                ('recent_donation', models.DateTimeField(blank=True, null=True)),
                ('total_donations', models.BinaryField(null=True)),
            ],
        ),
    ]
