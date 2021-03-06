# Generated by Django 4.0.2 on 2022-03-23 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kutuphane', '0003_alter_atikcodes_atikname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='atikcodes',
            name='atik_advice',
        ),
        migrations.RemoveField(
            model_name='atikcodes',
            name='atik_features',
        ),
        migrations.RemoveField(
            model_name='atikcodes',
            name='atikname',
        ),
        migrations.RemoveField(
            model_name='atikcodes',
            name='klavuz',
        ),
        migrations.RemoveField(
            model_name='atikcodes',
            name='where_to_go',
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='howDefineContent',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='howToReduceContent',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='img2',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='itsTtile',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='itsType',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='legislationlistContent',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='list1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='p1',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='p2',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='warningContent',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='atikcodes',
            name='whereAccoursContent',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
