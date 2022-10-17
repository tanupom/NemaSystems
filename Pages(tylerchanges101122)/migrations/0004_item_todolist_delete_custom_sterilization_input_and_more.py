# Generated by Django 4.1 on 2022-08-17 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Pages', '0003_custom_sterilization_input_delete_mymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('complete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Custom_Sterilization_input',
        ),
        migrations.AddField(
            model_name='item',
            name='todolist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Pages.todolist'),
        ),
    ]