# Generated by Django 3.2.8 on 2022-09-23 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_type',
            field=models.CharField(choices=[(1, 'التأشيرات'), (2, 'تذاكرطيران'), (3, 'تذاكربرية'), (4, 'تذاكربحرية'), (5, 'شحن'), (6, 'حجزفندقي'), (7, 'مستندات سفر'), (8, 'عمولات'), (9, 'تأمين صحي'), (10, 'رحلات')], max_length=3),
        ),
    ]
