import sys

try:
    from django.db import models
except Exception:
    print('Exception: Django Not Found, please install it with "pip install django".')
    sys.exit()


class channel_content(models.Model):
    from_name = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    data = models.DateTimeField()
    message_id = models.IntegerField()
    main_folder_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'channel_content'


class group_content(models.Model):
    from_name = models.TextField(null=True, blank=True)
    channel_text = models.TextField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video_duration = models.CharField(max_length=50, null=True, blank=True)
    data = models.DateTimeField()
    message_details = models.CharField(max_length=100)
    message_id = models.IntegerField()
    replied_message_details = models.CharField(max_length=100)
    replied_message_id = models.IntegerField()
    joined = models.BooleanField(default=True)
    filepath = models.TextField(null=True, blank=True)
    type_choices = [('url', 'url_type'), ('file', 'file_type'), ('video', 'video_type'), ('photo', 'photo_type'), ('audio', 'audio_type'), ('text', 'text_type')]
    type = models.CharField(max_length=10, choices=type_choices, default=type_choices[-1][0])
    parser_channel = models.ForeignKey(channel_content, to_field='id', on_delete=models.CASCADE, default=1)
    main_folder_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'group_content'

