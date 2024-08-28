# Generated by Django 5.1 on 2024-08-28 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('day_of_week', models.CharField(max_length=10)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.courses')),
                ('session_year_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.sessionyearmodel')),
                ('staff_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.staffs')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects')),
            ],
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_first_quarter', models.FloatField(default=0)),
                ('subject_second_quarter', models.FloatField(default=0)),
                ('subject_third_quarter', models.FloatField(default=0)),
                ('subject_fourth_quarter', models.FloatField(default=0)),
                ('subject_final_grade', models.FloatField(default=0)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.subjects')),
            ],
        ),
    ]
