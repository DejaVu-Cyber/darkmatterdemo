# Generated by Django 4.2.14 on 2024-07-17 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_collections', '0007_alter_collection_target_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection_target',
            name='last_modified',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]