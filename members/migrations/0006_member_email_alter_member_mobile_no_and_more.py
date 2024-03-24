# Generated by Django 4.2.1 on 2024-03-16 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_member_chamber_address_member_membership_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='nominee_dob',
            field=models.DateField(blank=True, null=True),
        ),
    ]