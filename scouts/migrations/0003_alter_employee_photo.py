# Generated by Django 3.2.7 on 2021-09-26 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scouts', '0002_alter_employee_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(upload_to='userprofile'),
        ),
    ]
