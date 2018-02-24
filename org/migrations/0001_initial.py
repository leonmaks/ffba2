# Generated by Django 2.0.2 on 2018-02-20 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrgUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='Datetime Created')),
                ('modify_dt', models.DateTimeField(auto_now=True, null=True, verbose_name='Datetime Modified')),
                ('name', models.CharField(max_length=500)),
                ('create_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orgunit_created_by', to=settings.AUTH_USER_MODEL)),
                ('modify_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='orgunit_modify_user', to=settings.AUTH_USER_MODEL)),
                ('up', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='org.OrgUnit')),
            ],
            options={
                'db_table': 'ffba_orgunit',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('social', models.URLField(blank=True, null=True)),
                ('orgunit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='org.OrgUnit')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'ffba_profile',
            },
        ),
    ]
