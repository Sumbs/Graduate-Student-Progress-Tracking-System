# Generated by Django 4.0.3 on 2022-05-11 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gspt_test', '0009_course_units'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coreq',
            old_name='new_course_id',
            new_name='current_course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='lab_id',
            new_name='lab',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='course_id',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='enrollment',
            old_name='student_no',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='adviser_id',
            new_name='adviser',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='curr_spec_id',
            new_name='current_specialization',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='deg_program_id',
            new_name='degree_program',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='lab_id',
            new_name='lab_affiliation',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='prev_spec_id',
            new_name='previous_specialization',
        ),
        migrations.RenameField(
            model_name='prereq',
            old_name='new_course_id',
            new_name='current_course',
        ),
    ]
