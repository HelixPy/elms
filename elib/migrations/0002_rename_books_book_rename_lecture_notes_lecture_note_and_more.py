# Generated by Django 4.1.3 on 2023-02-05 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elib', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='books',
            new_name='book',
        ),
        migrations.RenameModel(
            old_name='lecture_notes',
            new_name='lecture_note',
        ),
        migrations.RenameModel(
            old_name='messages',
            new_name='message',
        ),
        migrations.RenameModel(
            old_name='staffs',
            new_name='staff',
        ),
        migrations.RenameModel(
            old_name='students',
            new_name='student',
        ),
    ]
