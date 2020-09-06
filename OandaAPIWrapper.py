import json
import sys

import requests

class APIWrapper:
	def __init__(self, demo=True):
		with open(sys.argv[1]) as f:
			auth_tokens = json.load(f)
			self._id = auth_tokens['oanda_id']
			self._token = auth_tokens['oanda_token']
			# debug levelでmsg追加すべき
		self._api_endpoint = f'https://{}/v3/accounts/{}'
		self._stream_endpoint = f'https://{}/v3/accounts/{}'
		self._headers = {
			'Content-Type': 'application/json',
			'Authorization': f'Bearer {self._token}'
		}


if __name__ == '__main__':
	print('a,')
