# Generated by Django 5.0.3 on 2024-04-02 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friends',
            name='friend_name',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection', to='users.profile'), max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(to='users.profile'),
        ),
        migrations.AlterField(
            model_name='friends',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='connection', to='users.profile'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile'),
        ),
    ]
