# Generated by Django 3.2.5 on 2022-01-18 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Donor', '0002_fitness'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fitness',
        ),
        migrations.AddField(
            model_name='donor',
            name='discomforts',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='medications',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='donor',
            name='test_reports',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
