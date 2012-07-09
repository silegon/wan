from fabric.api import local

def sts():
    """
    start test server
    """
    local("python manage.py runserver 10.0.2.15:8000") 

def cwd():
    """
    change wplace database
    """
    local("python manage.py schemamigration wplace --auto")
    local("python manage.py migrate wplace")
