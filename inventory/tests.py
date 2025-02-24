from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
# Create your tests here.

# Function to log user actions
def log_user_activity(user, action, table_name, record_id=None):
    UserActivityLog.objects.create(
        user=user,
        action=action,
        table_name=table_name,
        record_id=record_id
    )
