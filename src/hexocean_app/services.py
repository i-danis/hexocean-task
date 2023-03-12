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
