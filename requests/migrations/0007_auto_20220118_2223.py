# Generated by Django 3.2.5 on 2022-01-18 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0006_auto_20220118_2222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='request',
            name='discomforts',
        ),
        migrations.RemoveField(
            model_name='request',
            name='medications',
        ),
        migrations.RemoveField(
            model_name='request',
            name='test_reports',
        ),
    ]
