#!/usr/bin/env python3

hostname = input('What is the hostname of your server: ')
#print(hostname)

if hostname == 'MTG' or 'mtg' or 'mTg' or 'MTg':
  print('The hostname was found to be ' + hostname)
  print('hostname matches expected config')
  print('Exiting the script')
