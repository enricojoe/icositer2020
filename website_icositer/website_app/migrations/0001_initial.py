# Generated by Django 3.2.5 on 2021-07-25 05:03

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=255)),
                ('isi', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('penulis', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name_plural': 'News',
                'db_table': 'News',
            },
        ),
    ]
