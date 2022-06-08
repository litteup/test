# Generated by Django 4.0.5 on 2022-06-08 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appone', '0002_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=200)),
                ('l_name', models.CharField(max_length=200)),
                ('specialization', models.CharField(max_length=500)),
                ('people', models.ManyToManyField(to='appone.people')),
            ],
        ),
    ]
