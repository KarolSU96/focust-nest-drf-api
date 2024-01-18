# Generated by Django 3.2 on 2024-01-18 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task_collections', '0002_remove_taskcollection_tasks'),
        ('tasks', '0003_rename_id_done_task_is_done'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_collection',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='task_collections.taskcollection'),
        ),
    ]
