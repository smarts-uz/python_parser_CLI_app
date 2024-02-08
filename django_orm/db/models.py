# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import sys


from django.db import models

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Execution(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    path = models.CharField(max_length=255, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'execution'


class SystemConfig(models.Model):
    id = models.BigIntegerField(primary_key=True, db_comment='1|41')
    key = models.TextField(db_comment='2|82')  # This field type is a guess.
    value = models.TextField(blank=True, null=True, db_comment='3|164')
    type = models.TextField(blank=True, null=True, db_comment='4|82')  # This field type is a guess.
    is_list = models.BooleanField(blank=True, null=True, db_comment='5|82')
    group = models.CharField(max_length=255, blank=True, null=True, db_comment='6|82')
    created_at = models.DateTimeField(blank=True, null=True, db_comment='7|82')
    updated_at = models.DateTimeField(blank=True, null=True, db_comment='8|82')
    deleted_at = models.DateTimeField(blank=True, null=True, db_comment='9|82')
    created_by = models.IntegerField(blank=True, null=True, db_comment='10|41')
    updated_by = models.IntegerField(blank=True, null=True, db_comment='11|41')
    deleted_by = models.IntegerField(blank=True, null=True, db_comment='12|41')
    name = models.CharField(max_length=255, blank=True, null=True, db_comment='13|82')

    class Meta:
        managed = False
        db_table = 'system_config'
        db_table_comment = '18'


class TgChannel(models.Model):
    from_name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    message_id = models.IntegerField()
    main_folder_name = models.CharField(max_length=100, blank=True, null=True)
    execution_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_channel'


class TgGroup(models.Model):
    channel_text = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    video_duration = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    message_details = models.CharField(max_length=100, blank=True, null=True)
    message_id = models.IntegerField(blank=True, null=True)
    replied_message_details = models.CharField(max_length=100, blank=True, null=True)
    replied_message_id = models.IntegerField(blank=True, null=True)
    joined = models.BooleanField(blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    main_folder_name = models.CharField(max_length=100, blank=True, null=True)
    tg_channel = models.ForeignKey(TgChannel, models.DO_NOTHING, blank=True, null=True)
    execution_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tg_group'
