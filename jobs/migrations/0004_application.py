# Generated by Django 4.2.16 on 2024-10-04 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0003_alter_job_work_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('short_description', models.TextField(blank=True)),
                ('last_jobs', models.TextField(blank=True)),
                ('cover_letter', models.TextField()),
                ('cv', models.FileField(blank=True, null=True, upload_to='cvs/')),
                ('cover_letter_file', models.FileField(blank=True, null=True, upload_to='cover_letters/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('under_review', 'Under Review'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='under_review', max_length=20)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.job')),
            ],
        ),
    ]
