# Generated by Django 4.2.1 on 2024-03-14 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_member_avatar_alter_member_blood_group_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='chamber_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='membership_category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='nominee_dob',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='nominee_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='nominee_relation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]