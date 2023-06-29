import api_init

api = api_init.api

def change_model(model_name):

    print("切换至模型{}", model_name)
    options = {}
    options['sd_model_checkpoint'] = model_name
    api.set_options(options)