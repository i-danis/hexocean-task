# Generated by Django 4.1.7 on 2023-03-10 13:36

from django.db import migrations


def init_data(apps, schema_editor):
    Size = apps.get_model("hexocean_app", "Size")

    size_200 = Size(height=200).save()
    size_400 = Size(height=400).save()

    Tier = apps.get_model("hexocean_app", "Tier")

    basic = Tier(
        title="basic",
    )
    basic.sizes.set([size_200])
    basic.save()

    premium = Tier(
        title="premium",
        full_size=True,
    )
    premium.sizes.set([size_200, size_400])
    premium.save()

    enterprise = Tier(
        title="enterprise",
        full_size=True,
        expired_link=True,
    )
    enterprise.sizes.set([size_200, size_400])
    enterprise.save()


class Migration(migrations.Migration):
    dependencies = [
        ("hexocean_app", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(init_data),
    ]
