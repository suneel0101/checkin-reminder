# Generated by Django 3.0.2 on 2020-01-28 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PingConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=250)),
                ('ping_text', models.CharField(max_length=250)),
                ('minutes_interval', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('start_timestamp', models.DateTimeField()),
                ('last_run_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=250)),
                ('response', models.CharField(blank=True, max_length=250, null=True)),
                ('timestamp_responded', models.DateTimeField(blank=True, null=True)),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ping.PingConfig')),
            ],
        ),
    ]
