import argparse
import subprocess
import concurrent.futures

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Flask app and tests')
    parser.add_argument('command', choices=['run', 'unit_test', 'webui_test'], help='Command to run')
    parser.add_argument('--app', default='UIapp.py', help='Flask app file')
    parser.add_argument('--webui_test', default='UIapp.py', help='Web UI test file')
    parser.add_argument('--unit_test', default='./UnitTest/UnitTest.py', help='Unit test file')

    args = parser.parse_args()

    if args.command == 'run':
        subprocess.run(['python', args.app])
    elif args.command == 'unit_test':
        subprocess.run(['python', args.unit_test])
    elif args.command == 'webui_test':
        webui_process = subprocess.Popen(['python', args.app])
        app_process = subprocess.Popen(['python', args.webui_test])
        app_process.wait()
        webui_process.terminate()