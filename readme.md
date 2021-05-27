```
print('hello world')
```
output: hello world
```
print("it does work, yay! let's try some other stuff, like making files.")
import os

local = '\\'.join(__file__.split('\\')[0:-1])
os.chdir(local)

print(os.listdir())
```
output: it does work, yay! let's try some other stuff, like making files.
['output.py', 'readme.md', 'scan.py']