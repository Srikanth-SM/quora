# Generated by Django 2.0 on 2019-01-02 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quora', '0002_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateField(auto_now=True),
        ),
    ]