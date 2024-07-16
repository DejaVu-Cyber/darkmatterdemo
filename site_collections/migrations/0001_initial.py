# Generated by Django 4.2.14 on 2024-07-16 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='collection_target',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('website', 'Website')], max_length=20)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('collected', models.BooleanField()),
                ('language', models.CharField(choices=[('English', 'English'), ('Mandarin', 'Mandarin')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('translated_url', models.URLField()),
                ('original_url', models.URLField()),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_collections.collection_target')),
            ],
        ),
    ]