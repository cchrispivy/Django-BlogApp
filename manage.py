#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import dotenv

if __name__ == '__main__':
    dotenv.read_dotenv('app.env')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings.common')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

