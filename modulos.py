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
	response = requests.get(f'http://api.ipstack.com/{enter_ip}?access_key=cf9d2c2dfec01449df2f0c34ddcfa1d4&format=1').content
	data = json.loads(response)
	so = platform.system()

	if so == 'Windows':
		clear = os.system('cls') or None

	elif so == 'Linux':
		clear = os.system('clear') or None
	print(f'\033[33m[\033[37m-\033[33m] Informations about IP: \033[36m{data["ip"]}\033[0;0m')
	line()
	print(f'''\033[33m[\033[37m-\033[33m] Type: \033[36m{data['type']}\033[0;0m
\033[33m[\033[37m-\033[33m] Continent_code: \033[36m{data['continent_code']}\033[0;0m
\033[33m[\033[37m-\033[33m] Continent_name: \033[36m{data['continent_name']}\033[0;0m
\033[33m[\033[37m-\033[33m] Country_code: \033[36m{data['country_code']}\033[0;0m
\033[33m[\033[37m-\033[33m]country_name: \033[36m{data['country_name']}\033[0;0m
\033[33m[\033[37m-\033[33m]Region_code: \033[36m{data['region_code']}\033[0;0m
\033[33m[\033[37m-\033[33m]Region_name : \033[36m{data['region_name']}\033[0;0m
\033[33m[\033[37m-\033[33m]City : \033[36m{data['city']}\033[0;0m
\033[33m[\033[37m-\033[33m]Zip : \033[36m{data['zip']}\033[0;0m
\033[33m[\033[37m-\033[33m]Latitude : \033[36m{data['latitude']}\033[0;0m
\033[33m[\033[37m-\033[33m]Longitude : \033[36m{data['longitude']}\033[0;0m''')
	line()
	#except:
		#print('it')