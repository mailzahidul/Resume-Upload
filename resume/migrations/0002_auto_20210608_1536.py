# Generated by Django 3.2.4 on 2021-06-08 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resume_info',
            old_name='date_of_birth',
            new_name='dob',
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('o', 'Others'), ('f', 'Female')], max_length=8),
        ),
        migrations.AlterField(
            model_name='resume_info',
            name='state',
            field=models.CharField(choices=[('khunla', 'Khulna'), ('borishal', 'Borishal'), ('chitfagram', 'Chitfagram'), ('rajshahi', 'Rajshahi'), ('rangpur', 'Rangpur'), ('dhaka', 'Dhaka')], max_length=20),
        ),
    ]