# Generated by Django 4.2.5 on 2023-09-24 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('skaters', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('skaters_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='skaters.skaters')),
            ],
            bases=('skaters.skaters',),
        ),
    ]
