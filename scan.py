from io import BytesIO
import subprocess
import sys
import os

local = '\\'.join(__file__.split('\\')[0:-1])
file = sys.argv[1]
os.chdir(local)

with open(file, 'r') as fh:
    data = fh.read()
fh.close()
with open('readme_temp.md', 'w') as fh:
    fh.write(data)
fh.close()
with open('readme_temp.md', 'r') as fh:
    lines = fh.readlines()
fh.close()

linstrs = ''.join(lines).split('code')
linstrs = str(linstrs).replace('[', '').replace(']', '').split('```')
os.remove('readme_temp.md')

code = str(linstrs[1])
print(code)

with open('output_temp.py', 'w') as fh:
    fh.write(code)
fh.close()
with open('output_temp.py', 'r') as fh:
    lines = fh.read()
lines = lines.replace('\\n', '\n')
with open('output_temp.py', 'w') as fh:
    fh.write(lines)
fh.close()

def codescan(file):
    process = subprocess.Popen([sys.executable, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    string = BytesIO(output).read().decode('utf-8').strip()

    return(string)

with open(file, 'r') as fh:
    data = fh.read()
data = data.replace('output', 'output: '+codescan('output_temp.py'))
with open('readme.md', 'w') as fh:
    fh.write(data)
fh.close()
os.remove('output_temp.py')