# Generated by Django 2.1.5 on 2019-03-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0009_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='skills',
            field=models.ManyToManyField(blank=True, to='skillMatch.Skill'),
        ),
    ]