# Generated by Django 4.0.3 on 2022-03-28 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_settlement_must_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='group_id',
            field=models.ForeignKey(default=64, on_delete=django.db.models.deletion.CASCADE, to='home.group'),
        ),
    ]