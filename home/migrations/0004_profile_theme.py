# Generated by Django 3.0.5 on 2020-04-23 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='theme',
            field=models.CharField(default='light', max_length=20),
            preserve_default=False,
        ),
    ]
