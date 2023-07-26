# Generated by Django 4.2.3 on 2023-07-25 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prompt', '0018_alter_subparagraph_subparagraph_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimplePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
    ]