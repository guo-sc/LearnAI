# coding: utf-8
# In[ ]:
import sys
import re
import os
import shutil
#import commands
import subprocess
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
  cmd = '7z a ' + zipfile + ' ' + ' '.join(paths)
  print("Command I'm going to do:" + cmd)
  #(status, output) = commands.getstatusoutput(cmd)
  # if status:
  #   sys.stderr.write(output)
  #   sys.exit(1)
  try:
    subprocess.check_call (cmd, shell=True,stderr=subprocess.STDOUT)
  except subprocess.CalledProcessError as e:
    raise RuntimeError ("command '{}' return with error (code {}): {}".format (e.cmd, e.returncode, e.output))


def main():
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit (1)

  todir = ''
  tozip = ''

  if args[0] == '--todir':
    todir = args[1]
  elif args[0] == '--tozip':
    tozip = args[1]
  elif len (args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit (1)
      
  dirs=args[2:]
  for dirname in dirs:
    result=get_special_paths (dirname)
    print(result)
    if todir == '':
      zip_to(result,tozip)
    else:
      copy_to (result, todir)

if __name__ == "__main__":
  main ()