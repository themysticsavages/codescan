from io import BytesIO
import subprocess
import sys
import os

local = '\\'.join(__file__.split('\\')[0:-1])
os.chdir(local)

with open(sys.argv[1], 'r') as fh0:
    text = fh0.readlines()
fh0.close()

text = list(filter(('```').__ne__, text))

fh1 = open('output.py', 'w')
ctext = []
i = 0


for string in text:
    nan = string.replace('```', '```\n')
    ctext.append(nan)

for texts in ctext:
        fh1.write(ctext[i])
        i += 1
fh1.close()

with open('output.py', 'r') as fh2:
    filedata = fh2.read()
filedata = filedata.replace('```', '').replace('\n\n', '\n')
with open('output.py', 'w') as fh3:
    fh3.write(filedata)
fh3.close()
fh2.close()
with open('output.py', 'r') as fh4:
    text1 = fh4.readlines()
fh4.close()

ttexts = ''
ttexts = ttexts.join(text1).split('\n\n')

def codescan(file):
    process = subprocess.Popen([sys.executable, file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    string = BytesIO(output).read().decode('utf-8').strip()

    return(string)

i = 0
returns = []

for texts in ttexts:
    if 'output' in ttexts[i]:
        pass
    else:
        fh5 = open('output.py', 'w').write(ttexts[i])
        if codescan('output.py') == '':
            print('(no output provided)')
        else:
            print(codescan('output.py'))
            returns.append(codescan('output.py'))
    i += 1

i = 0

f = open('readme.md', 'r')
filedata = f.read()
f.close()

while True:
    try:
        filedata = filedata.replace('output'+str(i), 'output: '+str(returns[i]))
        i += 1
    except IndexError:
        break

f = open('readme.md', 'w')
f.write(filedata)
f = open('readme.md', 'r')
filedata = f.read()

os.remove('output.py')
