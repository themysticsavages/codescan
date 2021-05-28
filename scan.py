from io import BytesIO
import platform
import subprocess
import sys
import os

# Linux users are people too! #
if platform.system() == 'Linux':
    local = os.path.dirname(os.path.realpath(__file__)) 
else:
    local = '\\'.join(__file__.split('\\')[0:-1]) # Since Linux doesn't use \\, I used something else #

file = sys.argv[1]
os.chdir(local)

with open(file, 'r') as fh: # Reads the file (doesn't have to be a .md file, it could be anything) #
    data = fh.read()
fh.close()
with open('readme_temp.md', 'w') as fh: # Creates a temporary copy to do whatever #
    fh.write(data)
fh.close()
with open('readme_temp.md', 'r') as fh: # Saves lines #
    lines = fh.readlines()
fh.close()

# Why did I have to do this ;( #
linstrs = ''.join(lines).split('//')
linstrs = str(linstrs).replace('[', '').replace(']', '').split('```')
os.remove('readme_temp.md')

code = str(linstrs[1]) # Takes a single code segment to avoid being the first release #
print(code)

with open('output_temp.py', 'w') as fh:
    fh.write(code)
fh.close()
with open('output_temp.py', 'r') as fh:
    lines = fh.read()
lines = lines.replace('\\n', '\n') # No unnescessary whitelines #
with open('output_temp.py', 'w') as fh:
    fh.write(lines)
fh.close()

# Made a function to make things seem easier #
def codescan(file):
    process = subprocess.Popen([sys.executable, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    string = BytesIO(output).read().decode('utf-8').strip()

    return(string)

# Where README #
with open(file, 'r') as fh:
    data = fh.read()
data = data.replace('output', 'output: '+codescan('output_temp.py'))
with open('readme.md', 'w') as fh:
    fh.write(data)
fh.close()
os.remove('output_temp.py')
