import http.client
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import json
connection = http.client.HTTPConnection('api.football-data.org')
headers = { 'X-Auth-Token': 'eeb803a8e99e46f3ae5fb83177d92ed7' }
connection.request('GET', '/v2/competitions/CL/matches', None, headers )
response = json.loads(connection.getresponse().read().decode())

print(response)

