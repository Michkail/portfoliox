# Generated by Django 3.2.4 on 2021-07-02 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BackStellar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelempiau', models.CharField(blank=True, max_length=75)),
                ('khinzir', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]