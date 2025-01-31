# Generated by Django 3.1.6 on 2021-02-25 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0012_auto_20210225_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='match',
            field=models.ManyToManyField(to='Tournament.Match'),
        ),
        migrations.AddField(
            model_name='tournament',
            name='round_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='match',
            name='round_number',
            field=models.IntegerField(),
        ),
    ]
