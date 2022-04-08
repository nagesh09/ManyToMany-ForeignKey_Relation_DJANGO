from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('auth_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=30)),

                ('book_name', models.CharField(max_length=32)),
                ('book_description', models.CharField(max_length=30)),

            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

                ('book_name', models.CharField(max_length=32)),
                ('book_description', models.CharField(max_length=30)),
                ('auth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testapp.author')),
                ('cat', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='testapp.category')),

                ('auth_name', models.CharField(max_length=32)),
                ('email', models.CharField(max_length=30)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='testapp.book')),

            ],
        ),
    ]
