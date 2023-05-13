from flask import Blueprint, jsonify, request
from webui import api_init
from app import config,utils
from webui import enums
import time

# webuiapi
img_api = api_init.api
# 创建蓝图
api = Blueprint('api', __name__)



# txt2img
@api.route('/txt2img', methods=['POST'])
def txt2img():
    data = request.get_json()
    print(data["base"])
    return jsonify({'code': 0, 'path': "static/imgs/1683434616_c156a544924063ed.png"})


@api.route('/get_img', methods=['POST'])
def get_img():
    #获取请求参数
    data = request.get_json()
    #print(data["optimize"])
    #生成图片名称
    img_name = utils.generate_filename('.png');
    #aim_path 是提供给前端访问的相对路径
    aim_path = config.relative_path + img_name;
    #file_path 是文件的绝对路径
    file_path = config.prefix_path + "/" + aim_path;
    #return ""


    # change sd model
    print(data["base"])
    model_name = enums.get_model_name(data["base"])
    options = {}
    options['sd_model_checkpoint'] = model_name
    print(model_name)
    img_api.set_options(options)


    # 生成图片
    seed = -1;
    if "" != data["seed"]:
        seed = data["seed"]

    result1 = img_api.txt2img(prompt=data["optimize"] + enums.get_lora_name(data["character"]),
                          negative_prompt=data["negative"],
                          seed=seed,
                          styles=["anime"],
                          cfg_scale=7,
                          sampler_name=data["sampling"],
                          steps=data["steps"],
                          #                      enable_hr=True,
                          #                      hr_scale=2,
                          #                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
                          #                      hr_second_pass_steps=20,
                          height=data["height"],
                          width=data["width"],
                          #                      denoising_strength=0.4,
                          )
    image_data = result1.image
    print(type(image_data))
    print(result1.info)
    image_data.save(file_path, "PNG")  # 保存为 PNG 格式
    time.sleep(2)
    return jsonify({'code': 0, 'path': aim_path})


# 定义第一个视图函数
@api.route('/users')
def get_users():
    return jsonify({'message': 'Hello, get_users!'})
    # 实现代码
    pass



# 定义第二个视图函数
@api.route('/users/<int:user_id>')
def get_user(user_id):
    # 实现代码
    pass

# 定义第三个视图函数
@api.route('/users', methods=['POST'])
def create_user():
    return jsonify({'message': 'Hello, world!'})
    # 实现代码
    pass
