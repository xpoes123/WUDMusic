# Generated by Django 5.1.3 on 2024-11-14 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('date_of_show', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('spotify', models.URLField(blank=True, null=True)),
                ('instagram', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='concert_images/')),
            ],
        ),
    ]
