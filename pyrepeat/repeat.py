#!/usr/bin/env python
import os
import time
import argparse
import datetime
import subprocess

# Major version, minor version
version = [int(x) for x in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'VERSION'), 'r').read().split('.')]

def _echo_summary(summary, interval) :
  print('[Running "{0:s}" every {1:d} seconds at {2:s}]'.format(summary, interval,
                           datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

def _repeat_command(num_repeat, repeat_interval, no_clear, no_except, command) :
  times_run = 0
  echo_summary = ' '.join(command)

  if no_clear :
    # print before running command to avoid repeating it without clearing
    _echo_summary(summary = echo_summary, interval = repeat_interval)

  while(num_repeat < 1 or (times_run < num_repeat)) :
    if not no_clear :
      subprocess.call(["clear"])
      _echo_summary(summary = echo_summary, interval = repeat_interval)

    try :
      subprocess.call(command)

      time.sleep(repeat_interval)
      times_run += 1
    except KeyboardInterrupt :
      if not no_except :
        print('\nStopping ...')
        break
      else :
        raise

def _parse_args() :
  # parameters are prefixed with --r to avoid collision with command being called
  args = argparse.ArgumentParser(description = 'Repeat command until stopped')
  args.add_argument('--num', '-n',        action='store',       dest='num_repeat',      default=0,  type=int, metavar='NUMBER',
                    help='Number of times to repeat command. Defaults to 0, which repeats forever.')
  args.add_argument('--interval', '-i',   action='store',       dest='repeat_interval', default=60, type=int, metavar='INTERVAL',
                    help='Sleep interval between command repetition in seconds, Defaults to 60.')
  args.add_argument('--command', '-c',    action='store',       dest='command',
                    help='Command to execute. Useful if the flags for the command clash with this utility\'s flags')
  args.add_argument('--no-clear', '-l',   action='store_true',  dest='noclear',
                    help='Do not clear screen between successive commands')
  args.add_argument('--version', '-v',    action='store_true',  dest='showversion',
                    help='Show version number and exit')
  args.add_argument('--no-except', '-x',  action='store_true',  dest='noexcept',
                    help='Do not catch keyboard interrupts')

  return args.parse_known_args()

def main() :
  (args, rem_cmd) = _parse_args()
  if args.command :
    # Use command from flag, ignoring extra flags/commands
    rem_cmd = args.command.strip()
    rem_cmd = rem_cmd.split(' ')

  if args.showversion :
    print('Repeat ' + '.'.join([str(x) for x in list(version)]))
  elif len(rem_cmd) > 0 :
    _repeat_command(num_repeat = args.num_repeat, repeat_interval = args.repeat_interval,
                    no_clear = args.noclear, no_except = args.noexcept, command = rem_cmd)
  else :
    print('No command to execute')

if '__main__' == __name__ :
  main()
