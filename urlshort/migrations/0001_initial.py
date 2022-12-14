# Generated by Django 3.2 on 2022-10-14 12:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLShort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('original_url', models.TextField()),
                ('slug', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'verbose_name': 'URL Short',
                'verbose_name_plural': 'URL Short',
            },
        ),
    ]
