import argparse
import subprocess
import concurrent.futures

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Flask app and tests')
    parser.add_argument('command', choices=['run', 'unit_test', 'webui_test'], help='Command to run')
    parser.add_argument('--app', default='UIapp.py', help='Flask app file')
    parser.add_argument('--webui_test', default='./WebUITest/webui_test.py', help='Web UI test file')
    parser.add_argument('--unit_test', default='./UnitTest/UnitTest.py', help='Unit test file')

    args = parser.parse_args()

    if args.command == 'run':
        subprocess.run(['python', args.app])


    elif args.command == 'unit_test':
        with open('unit_test_result.txt', 'w') as test_result:
            test_output = subprocess.Popen(['python', args.unit_test], stdout=test_result)
 
        with open('unit_test_result.txt') as file:
            unit_test_result = file.read()

        print("# Unit Test Results:")
        print(unit_test_result)           
        test_output.wait()

    
    elif args.command == 'webui_test':
        webui_process = subprocess.Popen(['python', args.app])
        with open('webui_test_result.txt', 'w') as test_result:
            test_output = subprocess.Popen(['python', args.webui_test], stdout=test_result)
            test_output.wait()
        webui_process.terminate()

        with open('webui_test_result.txt') as file:
            webui_test_result = file.read()

        print("# Web UI Test Results:")
        print(webui_test_result)



