# Generated by Django 4.1.3 on 2023-02-22 18:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elib', '0005_remove_staff_acc_status_remove_student_acc_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='gen_login',
            name='user_cart',
            field=models.CharField(default='student', max_length=15),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='book',
            name='date_uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='gen_login',
            name='last_login',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='leasing',
            name='date_collected',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='leasing',
            name='date_requested',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='leasing',
            name='date_returned',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='leasing',
            name='return_due_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='lecture_note',
            name='date_uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_sent',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_published',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='publication',
            name='date_uploaded',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='reading_list',
            name='date_added',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='staff',
            name='date_enrolled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_enrolled',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 22, 19, 54, 3, 695681, tzinfo=datetime.timezone.utc)),
        ),
    ]
