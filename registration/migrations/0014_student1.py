# Generated by Django 4.2.5 on 2023-10-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0013_delete_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(max_length=500)),
            ],
        ),
    ]
