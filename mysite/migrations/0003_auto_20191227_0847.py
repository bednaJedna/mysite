# Generated by Django 3.0.1 on 2019-12-27 07:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [("mysite", "0002_sidebaritems_display")]

    operations = [
        migrations.AlterField(
            model_name="content", name="text", field=tinymce.models.HTMLField()
        )
    ]
