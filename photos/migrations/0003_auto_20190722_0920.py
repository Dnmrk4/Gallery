# Generated by Django 2.2.3 on 2019-07-22 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20190722_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
