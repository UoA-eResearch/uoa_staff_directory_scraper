#!/usr/bin/env python3

import json
import os
import requests

with open('data.json') as f:
  data = json.load(f)

for p in data['profiles']:
  if 'upi' not in p:
    continue
  upi = p['upi']
  i = p['image'].replace('large', 'biggest')
  if i == '/people/imageraw/no-person/0/biggest' or os.path.exists('images/' + upi):
    continue
  r = requests.get('https://unidirectory.auckland.ac.nz' + i)
  ct = r.headers['content-type']
  if ct == 'image/png':
    ext = '.png'
  elif ct == 'image/jpg' or ct == 'image/jpeg':
    ext = '.jpg'
  else:
    print(ct)
    exit(1)
  os.makedirs('images/' + upi, exist_ok=True)
  filename = 'images/' + upi + '/' + upi + ext
  print(filename)
  with open(filename, 'wb') as f:
    f.write(r.content)
