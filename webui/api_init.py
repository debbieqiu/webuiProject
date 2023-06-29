import webuiapi,config

# create API client
#api = webuiapi.WebUIApi()

# create API client with custom host, port
#api = webuiapi.WebUIApi(host='172.23.182.18', port=81) #小右
api = webuiapi.WebUIApi(host=config.host, port=config.port)

# create API client with custom host, port and https
#api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# optionally set username, password when --api-auth is set on webui.
#api.set_auth('username', 'password')