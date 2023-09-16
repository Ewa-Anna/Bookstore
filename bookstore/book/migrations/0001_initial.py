# Generated by Django 4.2.5 on 2023-09-16 11:24

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
                ('catid', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('img_url', models.URLField()),
                ('catid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.category')),
            ],
            options={
                'ordering': ('-title',),
            },
        ),
    ]
