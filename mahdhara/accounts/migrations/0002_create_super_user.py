from django.utils import timezone
from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    def create_super_user(apps, schema_editor):
        from django.contrib.auth import get_user_model

        User = get_user_model()

        if User.objects.exclude():
            return

        superuser = User.objects.create_superuser(
            username="medsidatt",
            email="mdaloueimine@gmail.com",
            password="root",
            last_login=timezone.now()
        )

        superuser.save()

    operations = [
        migrations.RunPython(create_super_user)
    ]
