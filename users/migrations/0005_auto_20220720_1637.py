# Generated by Django 2.2.10 on 2022-07-20 16:37

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220720_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ssn',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=200)),
        ),
    ]
