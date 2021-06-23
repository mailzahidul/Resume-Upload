# Generated by Django 3.2.4 on 2021-06-23 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_auto_20210623_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume_info',
            name='profile_img',
            field=models.ImageField(blank=True, height_field='200', upload_to='profileimg/', width_field='200'),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='state',
            field=models.CharField(choices=[('rangpur', 'Rangpur'), ('dhaka', 'Dhaka'), ('rajshahi', 'Rajshahi'), ('chitfagram', 'Chitfagram'), ('borishal', 'Borishal'), ('khunla', 'Khulna')], max_length=20),
        ),
    ]