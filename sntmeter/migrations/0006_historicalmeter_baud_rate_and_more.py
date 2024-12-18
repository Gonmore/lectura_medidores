# Generated by Django 5.0.3 on 2024-04-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sntmeter', '0005_historicalmeter_pot_act_dir_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalmeter',
            name='baud_rate',
            field=models.IntegerField(blank=True, default=9600, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='corriente_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='corriente_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='corriente_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='fact_de_pot',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='fact_de_pot_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='fact_de_pot_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='fact_de_pot_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_apar_dir',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_apar_rev',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_reac_cap_QI',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_reac_cap_QII',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_reac_cap_QIII',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='pot_reac_cap_QIV',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='vol_de_fase_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='vol_de_fase_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='historicalmeter',
            name='vol_de_fase_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='baud_rate',
            field=models.IntegerField(blank=True, default=9600, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='corriente_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='corriente_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='corriente_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='fact_de_pot',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='fact_de_pot_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='fact_de_pot_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='fact_de_pot_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_apar_dir',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_apar_rev',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_reac_cap_QI',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_reac_cap_QII',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_reac_cap_QIII',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='pot_reac_cap_QIV',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='vol_de_fase_1',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='vol_de_fase_2',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
        migrations.AddField(
            model_name='meter',
            name='vol_de_fase_3',
            field=models.FloatField(blank=True, max_length=5, null=True),
        ),
    ]
