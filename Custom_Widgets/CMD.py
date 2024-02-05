import argparse
import textwrap

from Custom_Widgets.ProjectMaker import create_project
from Custom_Widgets.FileMonitor import start_file_listener, start_ui_conversion

def run_command():
    parser = argparse.ArgumentParser(description='Custom Widgets UI File Monitor')
    parser.add_argument('--monitor-ui', dest='file_to_monitor', help='Monitor changes made to UI file and generate new .py file and other necessary files for the custom widgets.')
    parser.add_argument('--convert-ui', dest='file_to_convert', help='Generate new .py file and other necessary files for the custom widgets.')
    parser.add_argument('--qt-library', dest='qt_library', help='Specify the Qt library (e.g., "PySide6")')

    parser.add_argument('--create-project', action='store_true', help='Create a new project')

    args = parser.parse_args()

    if args.file_to_monitor:
        start_file_listener(args.file_to_monitor, args.qt_library)
    
    elif args.file_to_convert:
        start_ui_conversion(args.file_to_convert, args.qt_library)

    elif args.create_project:
        create_project()

    else:
        print(textwrap.dedent("Use \n'Custom_Widgets --monitor-ui ui-path' \n'Custom_Widgets --convert-ui ui-path' \n'Custom_Widgets --create-project'"))