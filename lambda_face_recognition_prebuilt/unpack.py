from safe_extractor import safe_extractor
import os
import ctypes
import sys

deps_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deps.zip')
deps_install='/tmp/'

print("Unpacking '{}' into '{}'.".format(deps_path, deps_install))
safe_extractor.unzip_it(deps_path, deps_install)

print("Recursively loading all libs from '{}'.".format(deps_install))
for d, dirs, files in os.walk(deps_install):
    for f in files:
        if f.endswith('.a'):
            continue
        try:
            ctypes.cdll.LoadLibrary(os.path.join(d, f))
        except Exception as e:
            continue

print("Inserting '{}' into python's sys.path.".format(deps_install))
sys.path.insert(0, deps_install)
