# Generated by Django 4.2.5 on 2023-12-15 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0031_remove_student1_upload_remove_student1_user_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student1',
        ),
        migrations.AddField(
            model_name='student',
            name='file',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='uploads/'),
        ),
    ]
