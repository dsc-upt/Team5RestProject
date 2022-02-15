# Generated by Django 4.0.2 on 2022-02-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=256)),
                ('Description', models.TextField()),
                ('URL', models.URLField()),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.category')),
            ],
        ),
    ]
