# Generated by Django 4.2 on 2023-05-09 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dabbawala', '0018_cartitem_order_time_alter_cartitem_order_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
