# Generated by Django 4.0.3 on 2022-03-30 13:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gspt_test', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coreq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_course_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gspt_test.course')),
            ],
        ),
        migrations.CreateModel(
            name='Prereq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_course_id', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gspt_test.course')),
            ],
        ),
        migrations.DeleteModel(
            name='Pre_req',
        ),
    ]
