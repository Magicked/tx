#!/usr/bin/env python
import argparse
import os
import requests

from configparser import ConfigParser

from lib.constants import TX_VERSION, TX_HOME

from pytx.access_token import access_token
from pytx import ThreatPrivacyGroup

parser = argparse.ArgumentParser(description='Create a new Threat Privacy Group')
parser.add_argument('-n', '--name', action='store', required=True, dest='name',
    help='Create a Threat Privacy Group with the provided name')
parser.add_argument('-d', '--description', action='store', required=True, dest='description',
    help='Create a Threat Privacy Group with the provided name')

args = parser.parse_args()

try:
    config = ConfigParser()
    config.read(os.path.join(TX_HOME, 'etc', 'tx.ini'))
except ImportError:
    raise SystemExit('tx.ini was not found or was not accessible.')

app_id = config.get('auth', 'app_id')
app_secret = config.get('auth', 'app_secret')
access_token(app_id, app_secret)

response = requests.post('https://graph.facebook.com/v2.4/threat_privacy_groups?name={}&description={}&access_token={}|{}'.format(args.name, args.description, app_id, app_secret))

print(response.text)
