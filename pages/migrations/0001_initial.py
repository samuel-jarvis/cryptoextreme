# Generated by Django 2.1.1 on 2021-09-29 17:05

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_balance', models.IntegerField(blank=True, default='0')),
                ('bonus_balance', models.IntegerField(blank=True, default='0')),
                ('total_balance', models.IntegerField(blank=True, default='0')),
                ('profit_balance', models.IntegerField(blank=True, default='0')),
                ('active_deposit', models.IntegerField(blank=True, default='0')),
                ('last_deposit', models.IntegerField(blank=True, default='0')),
                ('total_deposit', models.IntegerField(blank=True, default='0')),
                ('pending_withdrawal', models.IntegerField(blank=True, default='0')),
                ('last_withdrawal', models.IntegerField(blank=True, default='0')),
                ('total_withdrawal', models.IntegerField(blank=True, default='0')),
                ('username', models.CharField(blank=True, default='0', max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('account_name', models.TextField(max_length=100)),
                ('bank_name', models.TextField(max_length=100)),
                ('account_number', models.IntegerField()),
                ('withdrawal_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('username', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Bitcoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('wallet', models.TextField(max_length=100)),
                ('withdrawal_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('username', models.CharField(default='0', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('phone', models.IntegerField(blank=True)),
                ('message', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Deposits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images/')),
                ('deposit_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Paypal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('email', models.TextField(max_length=100)),
                ('withdrawal_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('username', models.CharField(default='0', max_length=100)),
            ],
        ),
    ]
