# Generated by Django 2.2 on 2019-07-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0005_auto_20180126_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='subtotal',
            field=models.IntegerField(null=True),
        ),
    ]
