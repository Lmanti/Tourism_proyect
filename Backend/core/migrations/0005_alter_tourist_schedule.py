# Generated by Django 3.2.5 on 2021-07-14 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_user_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourist',
            name='schedule',
            field=models.CharField(max_length=30),
        ),
    ]
