# Generated by Django 2.1.5 on 2019-03-28 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0012_auto_20190328_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='skillMatch.Student'),
        ),
    ]