# Generated by Django 4.1.7 on 2023-05-05 10:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0011_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='item_sub_cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dabbawala.subcategory'),
        ),
    ]
