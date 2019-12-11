# Generated by Django 3.0 on 2019-12-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='student',
            name='collegeCareer',
            field=models.CharField(max_length=50, verbose_name='collegeCareer'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=50, verbose_name='Lastname'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='sex',
            field=models.CharField(max_length=25, verbose_name='Sex'),
        ),
    ]