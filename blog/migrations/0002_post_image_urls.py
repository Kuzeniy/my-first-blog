# Generated by Django 3.0 on 2019-12-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_urls',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
