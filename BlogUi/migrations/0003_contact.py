# Generated by Django 4.1.4 on 2022-12-30 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogUi', '0002_comment_date_alter_article_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name': 'Email',
            },
        ),
    ]
