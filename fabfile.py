from datetime import datetime
from fabric.api import *
from fabric.colors import green

env.user = 'ubuntu'
env.host_string = '167.99.110.46'
env.password = 'peperonchino2'
home_path = "/home/ubuntu"
project_name = "MentorTic"
backups_path = "/home/ubuntu/Ticbackup"
settings_staging = "--settings='config.settings.production'"
activate_env_staging = "source {}/ticenv/bin/activate".format(home_path)
manage = "python manage.py"


def deploy():
    print("Beginning Deploy:")
    with cd("{}/MentorTic".format(home_path)):
        run("git pull origin master")
        run("{} && pip install -r requirements.txt".format(activate_env_staging))
        run("{} && {} collectstatic --noinput {}".format(activate_env_staging, manage,
                                                         settings_staging))
        run("{} && {} migrate {}".format(activate_env_staging, manage, settings_staging))
        sudo("service nginx restart", pty=False)
        sudo("supervisorctl restart gunicorn_mentortic", pty=False)
    print(green("Deploy Tic successful"))


def createsuperuser():
    with cd("{}/MentorTic".format(home_path)):
        run("{} && {} createsuperuser {}".format(activate_env_staging, manage,
                                                 settings_staging))
        print(green("Createsuperuser cereza glup successful"))


def backup():
    today = datetime.today()
    backup_name = "backupglup-{}-{}-{}.sql".format(today.day, today.month, today.year)
    print("Beginning Backup:")
    with cd(backups_path):
        sudo("pg_dump {}db -U postgres -h localhost > {}".format(project_name, backup_name))
        get(backup_name, backup_name)
    print("Backup downloaded.")
