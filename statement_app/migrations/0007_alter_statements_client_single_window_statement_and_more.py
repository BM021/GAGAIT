# Generated by Django 4.1.3 on 2022-11-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement_app', '0006_alter_statements_client_single_window_statement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statements',
            name='client_single_window_statement',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='statements',
            name='client_statement',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]