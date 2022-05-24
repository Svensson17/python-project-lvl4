# Generated by Django 4.0.4 on 2022-05-15 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0003_task_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='performer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='performer', to=settings.AUTH_USER_MODEL, verbose_name='performer'),
        ),
    ]