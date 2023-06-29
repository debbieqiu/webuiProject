#模型名称配置
from enum import Enum

class BaseModel(Enum):
    AOM = 'aom'
    COUNTER = 'counterfeit'
    KAWAII = 'kawaii'


class LoraModel(Enum):
    LIYA = '达达利亚'
    AYATO = '神里绫人'
    DILUC = '迪卢克'
    HAYTHAM = '艾尔海森'


#autoDL 服务器配置
def get_model_name(model):
    if model == BaseModel.AOM.value:
        return "model.ckpt [89d59c3dde]"
    elif model == BaseModel.COUNTER.value:
        return "model.ckpt [89d59c3dde]"
    elif model == BaseModel.KAWAII:
        return "model.ckpt [89d59c3dde]"
    else:
        return "model.ckpt [89d59c3dde]"

# 小右 服务器配置
# def get_model_name(model):
#     if model == BaseModel.AOM.value:
#         return "手绘aom.safetensors [5493a0ec49]"
#     elif model == BaseModel.COUNTER.value:
#         return "手绘CounterfeitV25_25.safetensors [a074b8864e]"
#     elif model == BaseModel.KAWAII:
#         return "Wednesday"
#     else:
#         return "Invalid model"

#momo 服务器配置
# def get_model_name(model):
#
#     if model == BaseModel.AOM.value:
#         return "abyssorangemix3AOM3_aom3a1b.safetensors [5493a0ec49]"
#     elif model == BaseModel.COUNTER.value:
#         return "CounterfeitV25_25.safetensors [a074b8864e]"
#     elif model == BaseModel.KAWAII:
#         return "kawaii2D_kawaii2DV11Pruend.safetensors [ef0cb5e9b6]"
#     else:
#         return "Invalid model"

#小右
# def get_lora_name(model):
#     if model == LoraModel.DILUC.value:
#         return "<lora:c站迪卢克:1>"
#     elif model == LoraModel.AYATO.value:
#         return "<lora:haisen20-000008:1>"
#     elif model == LoraModel.LIYA.value:
#         return "<lora:利亚:1>"
#     elif model == LoraModel.HAYTHAM.value:
#         return "<lora:haisen20-000008:1>"
#     else:
#         return ""

# momo
# def get_lora_name(model):
#     if model == LoraModel.DILUC.value:
#         return "<lora:diluc122-000008:1>"
#     elif model == LoraModel.AYATO.value:
#         return "<lora:ayato_1tage-000008:1>"
#     elif model == LoraModel.HAYTHAM.value:
#         return "<lora:aihaytham_1tage:1>"
#     else:
#         return ""
