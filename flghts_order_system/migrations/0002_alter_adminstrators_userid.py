# Generated by Django 4.2.2 on 2023-06-06 13:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flghts_order_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminstrators',
            name='userId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flghts_order_system.users'),
        ),
    ]