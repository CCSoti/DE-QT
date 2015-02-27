from django.db import models


class MappingappBearingInclination(models.Model):
    bearing = models.IntegerField(blank=True)  # This field type is a guess.
    inclination = models.IntegerField(blank=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'mappingapp_bearing_inclination'


class MappingappCoordinates(models.Model):
    bng_ing = models.CharField(max_length=255, blank=True)
    grid_reference = models.CharField(max_length=20, blank=True)
    easting = models.IntegerField(blank=True)
    northing = models.IntegerField(blank=True)
    latitude = models.FloatField(blank=True)
    longitude = models.FloatField(blank=True)
    elevation = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_coordinates'


class MappingappCoreDetails(models.Model):
    exposure_core = models.CharField(max_length=255, blank=True)
    core_number = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_core_details'


class MappingappDocument(models.Model):
    docfile = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'mappingapp_document'


class MappingappLocationPhoto(models.Model):
    photo_site_id = models.IntegerField(blank=True)
    photo_ident_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_location_photo'


class MappingappOslSample(models.Model):
    stratigraphic_position = models.CharField(max_length=255, blank=True)
    lithofacies = models.CharField(max_length=255, blank=True)
    burial_depth = models.CharField(max_length=255, blank=True)
    lithology = models.CharField(max_length=255, blank=True)
    gamma_spec = models.CharField(max_length=255, blank=True)
    equipment_number = models.CharField(max_length=255, blank=True)
    probe_serial_no = models.CharField(max_length=255, blank=True)
    filename = models.CharField(max_length=255, blank=True)
    sample_time = models.CharField(max_length=255, blank=True)
    sample_duration = models.CharField(max_length=255, blank=True)
    potassium = models.CharField(max_length=255, blank=True)
    thorium = models.CharField(max_length=255, blank=True)
    uranium = models.CharField(max_length=255, blank=True)
    osl_sample_id = models.IntegerField(blank=True)
    osl_core_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_osl_sample'


class MappingappPhotoOf(models.Model):
    sample_pictured_id = models.IntegerField(blank=True)
    photo_idno_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_photo_of'


class MappingappPhotograph(models.Model):
    photo_filename = models.CharField(max_length=100, blank=True)
    photo_label = models.TextField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_photograph'


class MappingappRadiocarbonSample(models.Model):
    depth_below_sl = models.CharField(db_column='depth_below_SL', max_length=255, blank=True)
    material = models.TextField(blank=True)
    geological_setting = models.TextField(blank=True)
    stratigraphic_position_depth = models.CharField(max_length=255, blank=True)
    sample_weight = models.CharField(max_length=255, blank=True)
    pot_contamination = models.TextField(blank=True)
    calibration_curve = models.CharField(max_length=255, blank=True)
    c14_core_id = models.IntegerField(blank=True)
    c14_sample_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_radiocarbon_sample'


class MappingappRetreatZone(models.Model):
    zone_number = models.CharField(max_length=3, blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_retreat_zone'


class MappingappSampleBearingInclination(models.Model):
    sample_with_bearing_id = models.IntegerField(blank=True)
    bear_inc_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_sample_bearing_inclination'


class MappingappSampleSite(models.Model):
    collected_by = models.CharField(max_length=255, blank=True)
    site_name = models.CharField(max_length=255, blank=True)
    site_location = models.CharField(max_length=255, blank=True)
    county = models.CharField(max_length=255, blank=True)
    site_date = models.DateField(blank=True, null=True)
    operator = models.CharField(max_length=255, blank=True)
    geomorph_setting = models.TextField(blank=True)
    sample_type_collected = models.CharField(max_length=255, blank=True)
    photos_taken = models.TextField(blank=True)
    photographs = models.CharField(max_length=255, blank=True)
    site_notes = models.TextField(blank=True)
    site_coordinates_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_sample_site'


class MappingappTcnSample(models.Model):
    quartz_content = models.CharField(max_length=255, blank=True)
    sample_setting = models.TextField(blank=True)
    sampled_material = models.CharField(max_length=255, blank=True)
    boulder_dimensions = models.CharField(max_length=255, blank=True)
    sample_surface_strike_dip = models.CharField(max_length=255, blank=True)
    sample_thickness = models.CharField(max_length=255, blank=True)
    grain_size = models.CharField(max_length=255, blank=True)
    lithology = models.TextField(blank=True)
    tcn_sample_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_tcn_sample'


class MappingappTransect(models.Model):
    transect_number = models.CharField(max_length=2, blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_transect'


class MappingappSample(models.Model):
    sample_code = models.CharField(max_length=255, blank=True)
    sample_location_name = models.CharField(max_length=255, blank=True)
    collection_date = models.DateField(blank=True, null=True)
    collector = models.CharField(max_length=255, blank=True)
    sample_notes = models.TextField(blank=True)
    dating_priority = models.CharField(max_length=255, blank=True)
    age = models.IntegerField(blank=True)
    age_error = models.IntegerField(blank=True)
    calendar_age = models.IntegerField(blank=True)
    calendar_error = models.IntegerField(blank=True)
    lab_code = models.CharField(max_length=255, blank=True)
    sample_coordinates_id = models.ForeignKey(MappingappCoordinates)
    sample_site_id = models.IntegerField(blank=True)
    transect_id = models.ForeignKey(MappingappTransect)
    retreat_id = models.IntegerField(blank=True)

    class Meta:
        managed = True
        db_table = 'mappingapp_sample'


class MappingappUserprofile(models.Model):
    user_id = models.IntegerField()
    picture = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'mappingapp_userprofile'