# Generated by Django 2.0.1 on 2018-10-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0008_components'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.FileField(upload_to='')),
            ],
        ),
    ]
