# Generated by Django 2.2 on 2020-03-22 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0003_auto_20200322_0256'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_page',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
