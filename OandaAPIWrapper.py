import json
import sys

import requests

class APIWrapper:
	def __init__(self, demo=True):
		API_ROOT = switch_api_root(demo)
		STREAM_ROOT = switch_stream_root(demo)
		self._id, self._token = import_auth_info(sys.argv[1])
		self._api_endpoint = f'https://{API_ROOT}/v3/accounts/{self._id}'
		self._stream_endpoint = f'https://{STREAM_ROOT}/v3/accounts/{self._id}'
		self._headers = {
			'Content-Type': 'application/json',
			'Authorization': f'Bearer {self._token}'
		}

	def import_auth_info(self, auth_file):
		with open(auth_file) as f:
			auth_info = json.load(f)
			return (auth_info['oanda_id'], auth_info['oanda_token'])

	def switch_api_root(self, demo=True):
		if demo is True:
			return 'api-fxpractice.oanda.com'
		else:
			return 'api-fxtrade.oanda.com'

	def switch_stream_root(self, demo=True):
		if demo is True:
			return 'stream-fxpractice.oanda.com'
		else:
			return 'stream-fxtrade.oanda.com'


if __name__ == '__main__':
	pass
