#!/usr/bin/env python
"""Django's command-line utility for administrative tasks with enhanced error handling."""
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ordernow.settings')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        print(
            "Error: Django is not installed or the virtual environment is not activated.\n"
            "Ensure you have Django installed using:\n\n"
            "    pip install django\n\n"
            "If you are using a virtual environment, activate it before running this script:\n"
            "    source venv/bin/activate  # On macOS/Linux\n"
            "    venv\\Scripts\\activate   # On Windows"
        )
        sys.exit(1)

    try:
        execute_from_command_line(sys.argv)
    except Exception as e:
        print(f"An error occurred while executing the command: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
