# Generated by Django 2.2 on 2019-07-14 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0008_qty'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='qty',
            name='qty',
            field=models.PositiveSmallIntegerField(),
        ),
    ]