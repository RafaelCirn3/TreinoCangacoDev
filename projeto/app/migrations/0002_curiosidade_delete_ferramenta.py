# Generated by Django 4.1.7 on 2023-08-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curiosidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField()),
                ('descricao', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Ferramenta',
        ),
    ]
