#!/usr/bin/env python
import os
import time
import argparse
import datetime
import subprocess

# Major version, minor version
version = [int(x) for x in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION'), 'r').read().split('.')]

def _repeat_command(num_repeat, repeat_interval, no_summary, no_clear, command) :
  times_run = 0

  while(num_repeat < 1 or (times_run < num_repeat)) :
    if not no_clear :
      subprocess.call(["clear"])

    if not no_summary :
      echo_summary = ' '.join(command)
      print('[Running "{0:s}" every {1:d} seconds at {2:s}]'.format(echo_summary, repeat_interval,
                                         datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    subprocess.call(command)

    time.sleep(repeat_interval)
    times_run += 1

def _parse_args() :
  # parameters are prefixed with --r to avoid collision with command being called
  args = argparse.ArgumentParser(description = 'Repeat command until stopped')
  args.add_argument('--r-num', action='store', dest='num_repeat', default=0, type=int, metavar='NUMBER',
                    help='Number of times to repeat command. Defaults to 0, which repeats forever.')
  args.add_argument('--r-interval', action='store', dest='repeat_interval', default=60, type=int, metavar='INTERVAL',
                    help='Sleep interval between command repetition in seconds, Defaults to 60.')
  args.add_argument('--r-no-clear', action='store_true', dest='noclear', help='Do not clear screen between successive commands')
  args.add_argument('--r-no-summary', action='store_true', dest='nosummary', help='Do not show command summary before execution')
  args.add_argument('--r-version', action='store_true', dest='showversion', help='Show version number and exit')

  return args.parse_known_args()

def main() :
  (args, rem_cmd) = _parse_args()
  if args.showversion :
    print('Repeat ' + '.'.join([str(x) for x in list(version)]))
  elif len(rem_cmd) > 0 :
    _repeat_command(num_repeat = args.num_repeat, repeat_interval = args.repeat_interval,
                    no_summary = args.nosummary, no_clear = args.noclear, command = rem_cmd)
  else :
    print('No command to execute')

if '__main__' == __name__ :
  main()
