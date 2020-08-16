# Generated by Django 3.0.8 on 2020-08-16 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20200816_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='elevenbyfourteenprice',
            new_name='price',
        ),
        migrations.AddField(
            model_name='project',
            name='price2',
            field=models.FloatField(default=10.0, max_length=4),
            preserve_default=False,
        ),
    ]