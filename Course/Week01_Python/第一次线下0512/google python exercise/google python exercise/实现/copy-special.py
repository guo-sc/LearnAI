
# coding: utf-8

# In[ ]:


import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dirname):
  """Given a dirname, returns a list of all its special files."""
  result = []
  paths = os.listdir(dirname)  # list of paths in that dir
  for fname in paths:
    match = re.search(r'__(\w+)__', fname)
    if match:
      result.append(os.path.abspath(os.path.join(dirname, fname)))
  return result


def copy_to(paths, to_dir):
  """Copy all of the given files to the given dir, creating it if necessary."""
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    shutil.copy(path, os.path.join(to_dir, fname))
    # could error out if already exists os.path.exists():


def zip_to(paths, zipfile):
  """Zip up all of the given files into a new zip file with the given name."""
  cmd = 'zip -j ' + zipfile + ' ' + ' '.join(paths)
  print("Command I'm going to do:" + cmd)
  (status, output) = commands.getstatusoutput(cmd)
  # If command had a problem (status is non-zero),
  # print its output to stderr and exit.
  if status:
    sys.stderr.write(output)
    sys.exit(1)

