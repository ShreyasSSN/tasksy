# Generated by Django 5.1.1 on 2024-10-02 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_app', '0005_application_app_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='app_logo',
            field=models.ImageField(default='default.png', upload_to=''),
        ),
    ]
