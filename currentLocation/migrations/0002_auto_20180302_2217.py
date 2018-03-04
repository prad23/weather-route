# Generated by Django 2.0.2 on 2018-03-03 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('currentLocation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CNetwork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_text', models.CharField(max_length=15)),
                ('macaddress_text', models.CharField(max_length=50)),
                ('pub_date', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='cnetwork',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='currentLocation.Network'),
        ),
    ]