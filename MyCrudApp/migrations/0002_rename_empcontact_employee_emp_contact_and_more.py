# Generated by Django 5.1 on 2024-08-22 08:47

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyCrudApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='EmpContact',
            new_name='emp_contact',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpEmail',
            new_name='emp_email',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpName',
            new_name='emp_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpRole',
            new_name='emp_role',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='EmpSalary',
            new_name='emp_salary',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='Image',
            new_name='image',
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
