import sys
import argparse
import json2excel

# Main Menu
parser = argparse.ArgumentParser(prog='LinuxMDEparser.exe', usage='%(prog)s [command] [--option]')
subparsers = parser.add_subparsers(dest='Commands', title='Commands', help='Choose log filename to convert')
subparsers.required=True

# wdavhistory sub menu
wdavhistory = subparsers.add_parser('wdavhistory', help='File can be found on var\opt\microsoft\mdatp\wdavhistory from MDE logs folder')
wdavhistory.add_argument('--convert', dest='convert', help='Converts wdavhistory to wdavhistory.csv', action='store_true')

# real-time-protection.json sub menu
wdavhistory = subparsers.add_parser('real-time-protection', help='Troubleshoot performance issues for Microsoft Defender')
wdavhistory.add_argument('--convert', dest='convert', help='Converts real_time_protection.json to real_time_protection.csv', action='store_true')

if len(sys.argv) <= 1:
    sys.argv.append('--help')
