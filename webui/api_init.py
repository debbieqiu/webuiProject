import webuiapi

# create API client
#api = webuiapi.WebUIApi()

# create API client with custom host, port
#api = webuiapi.WebUIApi(host='172.23.182.18', port=81) #小右
api = webuiapi.WebUIApi(host='172.23.64.79', port=81)
# create API client with custom host, port and https
#api = webuiapi.WebUIApi(host='webui.example.com', port=443, use_https=True)

# create API client with default sampler, steps.
#api = webuiapi.WebUIApi(sampler='Euler a', steps=20)

# optionally set username, password when --api-auth is set on webui.
api.set_auth('username', 'password')