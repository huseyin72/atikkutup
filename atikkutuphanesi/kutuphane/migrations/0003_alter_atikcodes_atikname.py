# Generated by Django 4.0.2 on 2022-02-09 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutuphane', '0002_alter_atikcodes_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atikcodes',
            name='atikname',
            field=models.CharField(max_length=50),
        ),
    ]
