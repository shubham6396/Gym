# Generated by Django 3.0.4 on 2020-04-09 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffId', models.AutoField(db_column='STAFF_ID', primary_key=True, serialize=False, unique=True)),
                ('staffFirstName', models.CharField(db_column='STAFF_FIRST_NAME', max_length=100)),
                ('staffLastName', models.CharField(db_column='STAFF_LAST_NAME', max_length=100)),
                ('staffLoginName', models.CharField(db_column='STAFF_LOGIN_NAME', max_length=324)),
                ('staffPassword', models.CharField(db_column='STAFF_PASSWORD', max_length=100)),
                ('staffEmailId', models.CharField(db_column='STAFF_EMAIL_ID', max_length=324)),
                ('staffContact', models.CharField(db_column='STAFF_CONTACT', max_length=20)),
                ('staffRegistrationDate', models.DateTimeField(db_column='STAFF_REGISTRATION_DATE')),
            ],
            options={
                'db_table': 'STAFF',
            },
        ),
    ]
