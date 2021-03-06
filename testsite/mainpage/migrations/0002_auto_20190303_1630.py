# Generated by Django 2.1.7 on 2019-03-03 14:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boss',
            name='boss_position',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='employee_data',
            name='boss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boss', to='mainpage.Boss'),
        ),
    ]
