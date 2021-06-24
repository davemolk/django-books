# Generated by Django 3.2.3 on 2021-06-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_outlet', '0006_auto_20210624_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('code', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name_plural': 'Countries',
            },
        ),
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Address Entries'},
        ),
        migrations.AddField(
            model_name='book',
            name='published_countries',
            field=models.ManyToManyField(to='book_outlet.Country'),
        ),
    ]
