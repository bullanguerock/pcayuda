# Generated by Django 3.0.8 on 2020-07-05 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0003_auto_20200705_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='service',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
