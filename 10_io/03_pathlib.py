# Better approach to work with file paths
# irrespective of the operating system
# we use pathlib

from pathlib import Path
from pathlib import PurePath
from pathlib import PureWindowsPath
from pathlib import PurePosixPath

p = Path('..')

a = [print(x) for x in p.iterdir() if x.is_dir()]

# parts will divide the path into single unit
p = PurePath('/usr/bin/python3')
print(p.parts)

print(PureWindowsPath("/home/user/temp/1.py").root)
print(PurePosixPath("c:/user/1.py").root)


