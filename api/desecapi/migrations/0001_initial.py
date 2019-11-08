from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=191, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='desecapi.User')),
            ],
        ),
        migrations.CreateModel(
            name='RRset',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subname', models.CharField(blank=True, max_length=178)),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desecapi.Domain')),
            ],
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='desecapi.User')),
            ],
        ),
        migrations.AlterField(
            model_name='rrset',
            name='subname',
            field=models.CharField(blank=False, max_length=178),
        ),
    ]
