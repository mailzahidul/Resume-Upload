# Generated by Django 3.2.4 on 2021-06-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20210608_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_info',
            name='profile_img',
            field=models.ImageField(blank=True, height_field=200, upload_to='profileimg/', width_field=180),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='state',
            field=models.CharField(choices=[('dhaka', 'Dhaka'), ('rangpur', 'Rangpur'), ('borishal', 'Borishal'), ('khunla', 'Khulna'), ('rajshahi', 'Rajshahi'), ('chitfagram', 'Chitfagram')], max_length=20),
        ),
    ]
