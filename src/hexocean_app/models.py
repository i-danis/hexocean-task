import uuid
from io import BytesIO

from django.contrib.auth.models import AbstractUser
from django.core.files import File
from django.core.files.base import ContentFile
from django.db import models
from django.utils.html import mark_safe
from PIL import Image as PILImage


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    tier = models.ForeignKey("Tier", blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}"


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    content = models.ImageField(upload_to="images")
    image_array = models.ForeignKey(
        "ImageArray", related_name="images", on_delete=models.CASCADE
    )
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return f"{self.title}"

    def image_preview(self):
        return mark_safe(f'<img src = "{self.content.url}" width = "200"/>')

    def save(self, *args, **kwargs):
        self.resize((self.width, self.height))
        super().save(*args, **kwargs)

    def resize(self, size: tuple):
        im = PILImage.open(self.content)
        source_image = im.convert("RGB")
        source_image.thumbnail(size)
        output = BytesIO()
        source_image.save(output, format="png")
        output.seek(0)

        content_file = ContentFile(output.read())
        file = File(content_file)

        file_name = f"{self.image_array.pk}_{self.height}.png"
        self.content.save(file_name, file, save=False)


class ImageArray(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=200)

    user = models.ForeignKey(
        "User", related_name="image_arrays", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}"


class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    height = models.IntegerField()

    def __str__(self):
        return f"{self.height}"


class Tier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=100, unique=True)
    sizes = models.ManyToManyField("Size")
    is_expiration_link = models.BooleanField(default=False)
    full_size = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title}"
