import sys
import subprocess

subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'art'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pybase64'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'regex'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'selenium'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'webdriver-manager'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'dnspython'])


reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)