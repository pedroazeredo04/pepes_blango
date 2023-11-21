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

User.objects.filter(username=os.environ["pedrin_dj"]).exists() or \
    User.objects.create_superuser(os.environ["pedrin_dj"], os.environ["pedro_azeredo@usp.br"], os.environ["cavalobranco123"])
EOF