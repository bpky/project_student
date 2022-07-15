# Generated by Django 4.0.6 on 2022-07-14 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('contact', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=25)),
                ('is_verified', models.BooleanField(default=False, null=True)),
                ('verification_code', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'student_detail',
            },
        ),
        migrations.CreateModel(
            name='TrainingDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info.studentdetail')),
            ],
            options={
                'db_table': 'training_detail',
            },
        ),
        migrations.CreateModel(
            name='AcademicDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=200)),
                ('org_location', models.CharField(max_length=200)),
                ('academic_degree', models.CharField(max_length=200)),
                ('secured_mark', models.CharField(max_length=200)),
                ('position_category', models.CharField(max_length=200)),
                ('start_year', models.CharField(max_length=200)),
                ('end_year', models.CharField(max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_info.studentdetail')),
            ],
            options={
                'db_table': 'academic_detail',
            },
        ),
    ]