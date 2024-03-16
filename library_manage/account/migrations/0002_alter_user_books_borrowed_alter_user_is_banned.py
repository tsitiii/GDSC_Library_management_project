# Generated by Django 5.0.2 on 2024-03-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='books_borrowed',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_banned',
            field=models.BooleanField(default=False, null=True),
        ),
    ]