# Generated by Django 2.1.7 on 2019-04-20 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DateData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('total_messages', models.IntegerField()),
                ('total_customers', models.IntegerField()),
            ],
        ),
    ]
