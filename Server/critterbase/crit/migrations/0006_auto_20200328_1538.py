# Generated by Django 3.0.4 on 2020-03-28 20:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crit', '0005_auto_20200328_1537'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='northmonth',
            name='fish',
        ),
        migrations.RemoveField(
            model_name='northmonth',
            name='insect',
        ),
        migrations.RemoveField(
            model_name='southmonth',
            name='fish',
        ),
        migrations.RemoveField(
            model_name='southmonth',
            name='insect',
        ),
        migrations.DeleteModel(
            name='Fish',
        ),
        migrations.DeleteModel(
            name='Insect',
        ),
    ]
