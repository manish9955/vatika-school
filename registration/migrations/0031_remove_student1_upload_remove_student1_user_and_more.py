# Generated by Django 4.2.5 on 2023-12-15 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_alter_student1_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student1',
            name='upload',
        ),
        migrations.RemoveField(
            model_name='student1',
            name='user',
        ),
        migrations.AddField(
            model_name='student1',
            name='image1',
            field=models.ImageField(default=None, max_length=250, null=True, upload_to='uploads/'),
        ),
    ]