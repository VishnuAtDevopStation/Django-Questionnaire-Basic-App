# Generated by Django 2.1.1 on 2018-09-24 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(db_index=True, max_length=200)),
                ('answer', models.CharField(db_index=True, max_length=200)),
                ('option1', models.CharField(db_index=True, max_length=200)),
                ('option2', models.CharField(db_index=True, max_length=200)),
                ('option3', models.CharField(db_index=True, max_length=200)),
            ],
            options={
                'ordering': ('question',),
            },
        ),
    ]