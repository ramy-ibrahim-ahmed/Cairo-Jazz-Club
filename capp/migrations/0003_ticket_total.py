# Generated by Django 4.2.4 on 2023-08-11 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0002_remove_party_plan_remove_ticket_plan_ticket_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]