# Generated by Django 3.0.2 on 2020-01-18 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200116_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='photo_library',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='jumbo_bg',
            field=models.ImageField(default='default_bg', upload_to='profile/profile_backgrounds'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='default_profile.jpg', upload_to='profile/profile_images/'),
        ),
    ]