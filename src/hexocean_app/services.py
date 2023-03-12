import uuid

import redis

from hexocean_app.models import Image, ImageArray


def create_image_array(title, original_image, user):
    image_array = ImageArray(title=title, user=user)
    image_array.save()

    original_width, original_height = original_image.image.size
    for size in user.tier.sizes.all():
        new_height = size.height

        ratio = original_height / new_height
        new_width = round(original_width / ratio)
        image = Image(
            title=f"{title}_{new_height}",
            content=original_image,
            image_array=image_array,
            width=new_width,
            height=new_height,
        )
        image.save()

    if user.tier.full_size:
        image = Image(
            title=f"{title}_original",
            content=original_image,
            image_array=image_array,
            width=original_width,
            height=original_height,
        )
        image.save()

    image_array.refresh_from_db()

    return image_array


def create_expiration_link(original_link, expiration_time):
    redirect_base_url = "http://localhost:8000/hexocean-app/redirect/"
    expiry_token = str(uuid.uuid4())
    expiration_link = redirect_base_url + expiry_token
    r = redis.Redis(host="redis", port=6379)
    r.set(expiry_token, original_link, ex=expiration_time)
    return expiration_link
