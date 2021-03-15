# Generated by Django 3.1.4 on 2021-03-11 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('siteName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Fields',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('empID', models.IntegerField()),
                ('certificates', models.CharField(max_length=200)),
                ('yearOfCompletion', models.CharField(max_length=200)),
                ('siteID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Site', to='application.site')),
            ],
        ),
    ]