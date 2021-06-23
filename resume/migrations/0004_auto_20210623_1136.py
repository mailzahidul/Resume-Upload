# Generated by Django 3.2.4 on 2021-06-23 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_auto_20210623_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_info',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Others')], max_length=8),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='profile_img',
            field=models.ImageField(blank=True, height_field='200', upload_to='profileimg/', width_field='180'),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='state',
            field=models.CharField(choices=[('borishal', 'Borishal'), ('chitfagram', 'Chitfagram'), ('khunla', 'Khulna'), ('dhaka', 'Dhaka'), ('rajshahi', 'Rajshahi'), ('rangpur', 'Rangpur')], max_length=20),
        ),
    ]
