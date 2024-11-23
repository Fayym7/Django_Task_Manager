# Generated by Django 5.0.4 on 2024-11-22 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_oauthkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleOAuthKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Friendly name for this key configuration', max_length=255)),
                ('client_id', models.CharField(help_text='Google OAuth Client ID', max_length=255)),
                ('client_secret', models.CharField(help_text='Google OAuth Client Secret', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInvitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('token', models.CharField(blank=True, max_length=50, unique=True)),
                ('is_used', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
