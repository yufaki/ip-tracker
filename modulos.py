def line():
	print('\033[35m===\033[0;0m'*18)


def ip_tracker():
	#try:
	import json
	import requests
	import platform
	import os
	global enter_ip
	enter_ip = str(input('IP: '))
	response = requests.get(f'http://ip-api.com/json/{enter_ip}').content
	data = json.loads(response)
	so = platform.system()

	if so == 'Windows':
		clear = os.system('cls') or None

	elif so == 'Linux':
		clear = os.system('clear') or None
	print(f'\033[33m[\033[37m-\033[33m] Informations about IP: \033[36m{data["query"]}\033[0;0m')
	line()
	print(f'''\033[33m[\033[37m-\033[33m] Status: \033[36m{data['status']}\033[0;0m
\033[33m[\033[37m-\033[33m] Country: \033[36m{data['country']}\033[0;0m
\033[33m[\033[37m-\033[33m] CountryCode: \033[36m{data['countryCode']}\033[0;0m
\033[33m[\033[37m-\033[33m] Region: \033[36m{data['region']}\033[0;0m
\033[33m[\033[37m-\033[33m] RegionName: \033[36m{data['regionName']}\033[0;0m
\033[33m[\033[37m-\033[33m] City: \033[36m{data['city']}\033[0;0m
\033[33m[\033[37m-\033[33m] Zip: \033[36m{data['zip']}\033[0;0m
\033[33m[\033[37m-\033[33m] Lat: \033[36m{data['lat']}\033[0;0m
\033[33m[\033[37m-\033[33m] Lon: \033[36m{data['lon']}\033[0;0m
\033[33m[\033[37m-\033[33m] Timezone: \033[36m{data['timezone']}\033[0;0m
\033[33m[\033[37m-\033[33m] Isp: \033[36m{data['isp']}\033[0;0m
\033[33m[\033[37m-\033[33m] Org: \033[36m{data['org']}\033[0;0m
\033[33m[\033[37m-\033[33m] As: \033[36m{data['as']}\033[0;0m''')
	line()
	#except:
		#print('it')