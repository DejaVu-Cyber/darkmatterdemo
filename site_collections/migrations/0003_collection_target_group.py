# Generated by Django 4.2.14 on 2024-07-16 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_group_user_collection_manager_user_group'),
        ('site_collections', '0002_collection_target_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection_target',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.group'),
        ),
    ]
