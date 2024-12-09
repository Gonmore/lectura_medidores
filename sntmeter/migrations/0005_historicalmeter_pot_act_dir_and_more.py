# Generated by Django 5.0.3 on 2024-04-04 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sntmeter', '0004_alter_historicalmeter_con_ip_alter_meter_con_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_act_dir',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_act_rev',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_act_dir',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_act_rev',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalmeter',
            name='serial',
            field=models.CharField(default='NoS/N', max_length=50),
        ),
        migrations.AlterField(
            model_name='meter',
            name='serial',
            field=models.CharField(default='NoS/N', max_length=50),
        ),
    ]
