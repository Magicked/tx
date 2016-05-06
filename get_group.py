#!/usr/bin/env python
import argparse
import os
import requests

from configparser import ConfigParser

from lib.constants import TX_VERSION, TX_HOME

from pytx.access_token import access_token
from pytx import ThreatPrivacyGroup

parser = argparse.ArgumentParser(description='Print the Threat Privacy Groups you have membership to.')

try:
    config = ConfigParser()
    config.read(os.path.join(TX_HOME, 'etc', 'tx.ini'))
except ImportError:
    raise SystemExit('tx.ini was not found or was not accessible.')

app_id = config.get('auth', 'app_id')
app_secret = config.get('auth', 'app_secret')
access_token(app_id, app_secret)

results = ThreatPrivacyGroup.mine(role='member', full_response=True)
print(results)
