# Generated by Django 4.2.11 on 2024-05-13 14:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="users",
            options={
                "verbose_name": "Пользователи",
                "verbose_name_plural": "Пользователи",
            },
        ),
        migrations.AddField(
            model_name="users",
            name="email",
            field=models.EmailField(default="-", max_length=254),
        ),
        migrations.AlterField(
            model_name="users",
            name="password",
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name="users",
            name="username",
            field=models.CharField(max_length=150),
        ),
    ]
