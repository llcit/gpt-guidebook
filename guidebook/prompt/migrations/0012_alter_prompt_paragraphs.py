# Generated by Django 4.2.2 on 2023-07-11 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("prompt", "0011_alter_prompt_paragraphs"),
    ]

    operations = [
        migrations.AlterField(
            model_name="prompt",
            name="paragraphs",
            field=models.ManyToManyField(blank=True, to="prompt.paragraph"),
        ),
    ]
