# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MappingappBearingInclination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bearing', models.IntegerField(blank=True)),
                ('inclination', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_bearing_inclination',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappCoordinates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bng_ing', models.CharField(max_length=255, blank=True)),
                ('grid_reference', models.CharField(max_length=20, blank=True)),
                ('easting', models.IntegerField(blank=True)),
                ('northing', models.IntegerField(blank=True)),
                ('latitude', models.FloatField(blank=True)),
                ('longitude', models.FloatField(blank=True)),
                ('elevation', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mappingapp_coordinates',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappCoreDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('exposure_core', models.CharField(max_length=255, blank=True)),
                ('core_number', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'mappingapp_core_details',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappDocument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('docfile', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mappingapp_document',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappLocationPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo_site_id', models.IntegerField(blank=True)),
                ('photo_ident_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_location_photo',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappOslSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stratigraphic_position', models.CharField(max_length=255, blank=True)),
                ('lithofacies', models.CharField(max_length=255, blank=True)),
                ('burial_depth', models.CharField(max_length=255, blank=True)),
                ('lithology', models.CharField(max_length=255, blank=True)),
                ('gamma_spec', models.CharField(max_length=255, blank=True)),
                ('equipment_number', models.CharField(max_length=255, blank=True)),
                ('probe_serial_no', models.CharField(max_length=255, blank=True)),
                ('filename', models.CharField(max_length=255, blank=True)),
                ('sample_time', models.CharField(max_length=255, blank=True)),
                ('sample_duration', models.CharField(max_length=255, blank=True)),
                ('potassium', models.CharField(max_length=255, blank=True)),
                ('thorium', models.CharField(max_length=255, blank=True)),
                ('uranium', models.CharField(max_length=255, blank=True)),
                ('osl_sample_id', models.IntegerField(blank=True)),
                ('osl_core_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_osl_sample',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappPhotograph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo_filename', models.CharField(max_length=100, blank=True)),
                ('photo_label', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_photograph',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappPhotoOf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_pictured_id', models.IntegerField(blank=True)),
                ('photo_idno_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_photo_of',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappRadiocarbonSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('depth_below_sl', models.CharField(max_length=255, db_column=b'depth_below_SL', blank=True)),
                ('material', models.TextField(blank=True)),
                ('geological_setting', models.TextField(blank=True)),
                ('stratigraphic_position_depth', models.CharField(max_length=255, blank=True)),
                ('sample_weight', models.CharField(max_length=255, blank=True)),
                ('pot_contamination', models.TextField(blank=True)),
                ('calibration_curve', models.CharField(max_length=255, blank=True)),
                ('c14_core_id', models.IntegerField(blank=True)),
                ('c14_sample_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_radiocarbon_sample',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappRetreatZone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zone_number', models.CharField(max_length=3, blank=True)),
            ],
            options={
                'db_table': 'mappingapp_retreat_zone',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_code', models.CharField(max_length=255, blank=True)),
                ('sample_location_name', models.CharField(max_length=255, blank=True)),
                ('collection_date', models.DateField(null=True, blank=True)),
                ('collector', models.CharField(max_length=255, blank=True)),
                ('sample_notes', models.TextField(blank=True)),
                ('dating_priority', models.CharField(max_length=255, blank=True)),
                ('age', models.IntegerField(blank=True)),
                ('age_error', models.IntegerField(blank=True)),
                ('calendar_age', models.IntegerField(blank=True)),
                ('calendar_error', models.IntegerField(blank=True)),
                ('lab_code', models.CharField(max_length=255, blank=True)),
                ('sample_site_id', models.IntegerField(blank=True)),
                ('retreat_id', models.IntegerField(blank=True)),
                ('sample_coordinates_id', models.ForeignKey(to='mappingapp.MappingappCoordinates')),
            ],
            options={
                'db_table': 'mappingapp_sample',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappSampleBearingInclination',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sample_with_bearing_id', models.IntegerField(blank=True)),
                ('bear_inc_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_sample_bearing_inclination',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappSampleSite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('collected_by', models.CharField(max_length=255, blank=True)),
                ('site_name', models.CharField(max_length=255, blank=True)),
                ('site_location', models.CharField(max_length=255, blank=True)),
                ('county', models.CharField(max_length=255, blank=True)),
                ('site_date', models.DateField(null=True, blank=True)),
                ('operator', models.CharField(max_length=255, blank=True)),
                ('geomorph_setting', models.TextField(blank=True)),
                ('sample_type_collected', models.CharField(max_length=255, blank=True)),
                ('photos_taken', models.TextField(blank=True)),
                ('photographs', models.CharField(max_length=255, blank=True)),
                ('site_notes', models.TextField(blank=True)),
                ('site_coordinates_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_sample_site',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappTcnSample',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quartz_content', models.CharField(max_length=255, blank=True)),
                ('sample_setting', models.TextField(blank=True)),
                ('sampled_material', models.CharField(max_length=255, blank=True)),
                ('boulder_dimensions', models.CharField(max_length=255, blank=True)),
                ('sample_surface_strike_dip', models.CharField(max_length=255, blank=True)),
                ('sample_thickness', models.CharField(max_length=255, blank=True)),
                ('grain_size', models.CharField(max_length=255, blank=True)),
                ('lithology', models.TextField(blank=True)),
                ('tcn_sample_id', models.IntegerField(blank=True)),
            ],
            options={
                'db_table': 'mappingapp_tcn_sample',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappTransect',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('transect_number', models.CharField(max_length=2, blank=True)),
            ],
            options={
                'db_table': 'mappingapp_transect',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MappingappUserprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('picture', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'mappingapp_userprofile',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='mappingappsample',
            name='transect_id',
            field=models.ForeignKey(to='mappingapp.MappingappTransect'),
            preserve_default=True,
        ),
    ]
