#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python manage.py migrate

# create superuser if missing
cat <<EOF | python manage.py shell
import os
from django.contrib.auth import get_user_model

User = get_user_model()

# Verificar se as chaves do ambiente estão definidas antes de acessá-las
username = os.environ.get("pedrin_dj")
email = os.environ.get("pedro_azeredo@usp.br")
password = os.environ.get("cavalobranco123")

if username and email and password:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
EOF