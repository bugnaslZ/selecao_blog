# Generated by Django 5.1.4 on 2024-12-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_tester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tester',
            name='context',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='tester',
            name='domain',
            field=models.CharField(max_length=220),
        ),
        migrations.AlterField(
            model_name='tester',
            name='title',
            field=models.CharField(max_length=220),
        ),
    ]
