# Generated by Django 3.2.15 on 2022-08-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220801_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
