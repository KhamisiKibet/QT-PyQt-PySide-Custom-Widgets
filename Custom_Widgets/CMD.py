import argparse
import textwrap

from . ProjectMaker import create_project
from . FileMonitor import start_file_listener

def run_command():
    parser = argparse.ArgumentParser(description='Custom Widgets UI File Monitor')
    parser.add_argument('--monitor-ui', dest='file_to_monitor', help='Monitor changes made to UI file and generate new .py file')
    parser.add_argument('--qt-library', dest='qt_library', help='Specify the Qt library (e.g., "PySide6")')

    parser.add_argument('--create-project', action='store_true', help='Create a new project')

    args = parser.parse_args()

    if args.file_to_monitor:
        start_file_listener(args.file_to_monitor, args.qt_library)
    
    elif args.create_project:
        create_project()

    else:
        print(textwrap.dedent("Use \n'Custom_Widgets --monitor-ui ui-path' \n'Custom_Widgets --create-project'"))