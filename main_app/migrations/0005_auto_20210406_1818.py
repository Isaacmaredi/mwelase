# Generated by Django 3.1.7 on 2021-04-06 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210406_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('NOT_STARTED', 'Not Started'), ('IN_PROGRESS_DELAYED', 'Delayed'), ('IN_PROGRESS_ON_TRACK', 'On Track'), ('TERMINATED', 'Terminated'), ('COMPLETED', 'Completed')], default='NS', max_length=30),
        ),
    ]
