# Generated by Django 3.2.3 on 2021-07-10 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_tag_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]