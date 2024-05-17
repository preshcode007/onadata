# Generated by Django 3.2.23 on 2024-01-22 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('viewer', '0002_alter_export_export_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericExport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('export_type', models.CharField(choices=[('xlsx', 'Excel'), ('csv', 'CSV'), ('zip', 'ZIP'), ('kml', 'kml'), ('csv_zip', 'CSV ZIP'), ('sav_zip', 'SAV ZIP'), ('sav', 'SAV'), ('external', 'Excel'), ('osm', 'osm'), ('gsheets', 'Google Sheets'), ('geojson', 'geojson')], default='xlsx', max_length=10)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('filename', models.CharField(blank=True, max_length=255, null=True)),
                ('filedir', models.CharField(blank=True, max_length=255, null=True)),
                ('task_id', models.CharField(blank=True, max_length=255, null=True)),
                ('time_of_last_submission', models.DateTimeField(default=None, null=True)),
                ('internal_status', models.SmallIntegerField(default=0)),
                ('export_url', models.URLField(default=None, null=True)),
                ('options', models.JSONField(default=dict)),
                ('error_message', models.CharField(blank=True, max_length=255, null=True)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
            options={
                'abstract': False,
                'unique_together': {('content_type', 'object_id', 'filename')},
            },
        ),
    ]