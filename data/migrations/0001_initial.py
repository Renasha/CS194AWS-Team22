# Generated by Django 3.2.9 on 2022-05-09 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='userprofile',
            fields=[
                ('consumer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=100)),
                ('track', models.CharField(max_length=400)),
                ('totalUnits', models.IntegerField(default=0)),
                ('degreeProgress', models.IntegerField(default=0)),
                ('transcript_json', models.JSONField()),
            ],
        ),
    ]
