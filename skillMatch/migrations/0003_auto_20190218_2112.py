# Generated by Django 2.1.5 on 2019-02-18 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0002_student_computing_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='computing_id',
            field=models.CharField(max_length=6, unique=True),
        ),
    ]
