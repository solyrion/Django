# Generated by Django 4.0.5 on 2022-08-07 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memo_text', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
