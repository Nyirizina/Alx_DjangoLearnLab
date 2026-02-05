# No-op migration: changes consolidated into 0001_initial
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0002_alter_book_options_customuser'),
    ]

    operations = [
    ]
