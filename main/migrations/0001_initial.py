# Generated by Django 4.0.4 on 2022-04-18 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_id', models.CharField(max_length=255, unique=True)),
                ('blog_name', models.CharField(max_length=255)),
                ('blog_rank', models.CharField(max_length=255)),
                ('search_rank', models.CharField(max_length=255)),
                ('blog_link', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'blog_rank',
                'managed': True,
            },
        ),
    ]
