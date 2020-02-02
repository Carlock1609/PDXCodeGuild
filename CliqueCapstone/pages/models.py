from django.db import models
from users.models import CustomUser, UserProfile


from django.db.models.signals import post_save
from PIL import Image
import uuid # S3 bucket

import datetime
from django.utils import timezone

# Create your models here.

