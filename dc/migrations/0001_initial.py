# Generated by Django 3.1 on 2020-09-01 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('amount', models.IntegerField(default=1)),
                ('money', models.DecimalField(decimal_places=0, max_digits=7)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DebitItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('amount', models.IntegerField(default=1)),
                ('money', models.DecimalField(decimal_places=0, max_digits=7)),
                ('date', models.DateField()),
            ],
        ),
    ]