# Generated by Django 3.0.4 on 2020-04-06 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Two', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idcard',
            name='id_person',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Two.Person'),
        ),
    ]