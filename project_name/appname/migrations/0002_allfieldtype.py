# Generated by Django 5.1 on 2024-09-06 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllFieldType',
            fields=[
                ('auto_field', models.AutoField(primary_key=True, serialize=False)),
                ('big_integer_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=255)),
                ('date_field', models.DateField()),
                ('date_time_field', models.DateTimeField()),
                ('decimal_field', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration_field', models.DurationField()),
                ('email_field', models.EmailField(max_length=254)),
                ('file_field', models.FileField(upload_to='uploads/')),
                ('float_field', models.FloatField()),
                ('image_field', models.ImageField(upload_to='images/')),
                ('integer_field', models.IntegerField()),
                ('generic_ip_address_field', models.GenericIPAddressField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('positive_small_integer_field', models.PositiveSmallIntegerField()),
                ('slug_field', models.SlugField()),
                ('small_integer_field', models.SmallIntegerField()),
                ('text_field', models.TextField()),
                ('time_field', models.TimeField()),
                ('url_field', models.URLField()),
                ('uuid_field', models.UUIDField()),
            ],
        ),
    ]
