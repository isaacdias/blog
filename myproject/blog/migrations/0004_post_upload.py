# Generated by Django 2.2.5 on 2019-09-21 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(default=2, upload_to='static/imgs/'),
            preserve_default=False,
        ),
    ]
