# Generated by Django 2.1.5 on 2019-04-01 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skillMatch', '0009_auto_20190331_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='picture',
            field=models.ImageField(default='static/default-user.jpg', upload_to='images/'),
        ),
    ]