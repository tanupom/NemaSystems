# Generated by Django 4.1 on 2022-08-28 02:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Pages', '0005_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('ad_space', models.CharField(max_length=100)),
                ('format', models.CharField(choices=[('FN', 'FORMAT_NATIVE'), ('FNB', 'FORMAT_NATIVE_BANNER'), ('FI', 'FORMAT_INTERSTITIAL'), ('FB', 'FORMAT_BANNER'), ('FMR', 'FORMAT_MEDIUM,RECT'), ('FRV', 'FORMAT_REWARDED_VIDEO')], default='FN', max_length=3)),
                ('pid', models.CharField(default='', max_length=50)),
                ('cpm', models.IntegerField(default=0)),
                ('source', models.CharField(choices=[('FB', 'FACEBOOK'), ('G', 'GOOGLE')], default='FB', max_length=2)),
                ('comments', models.TextField(default='')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='placeid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Publisher',
        ),
    ]
