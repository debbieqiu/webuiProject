from flask import Blueprint, jsonify, request
from webui import model, txt2img
from app import config, utils, enums
import time

# 创建蓝图
api = Blueprint('api', __name__)


# txt2img
@api.route('/txt2img', methods=['GET'])
def get_img_test():
    result1 = txt2img.get_img("1girl", "", "", 1234, "Euler a", 30, 512, 512)

    print(result1.image)
    return "ok"


@api.route('/get_img', methods=['POST'])
def get_img():
    # 获取请求参数
    data = request.get_json()
    # print(data["optimize"])
    # 生成图片名称
    img_name = utils.generate_filename('.png');
    # aim_path 是提供给前端访问的相对路径
    aim_path = config.relative_path + img_name;
    # file_path 是文件的绝对路径
    file_path = config.prefix_path + "/" + aim_path;

    # change sd model
    print("切换基础模型{}", data["base"])
    model_name = enums.get_model_name(data["base"])
    model.change_model(model_name)

    # 获取lora参数
    lora = enums.get_lora_name(data["character"])
    # 获取seed
    seed = -1
    if "" != data["seed"]:
        seed = data["seed"]
    # 调用gpu服务器
    result1 = txt2img.txt2img(data["optimize"], lora, data["negative"], seed, data["sampling"], data["steps"],
                              data["height"], data["width"])
    # 解析绘制的图像数据
    image_data = result1.image
    print(type(image_data))
    print(result1.info)
    # 存储图像到本地
    image_data.save(file_path, "PNG")  # 保存为 PNG 格式
    time.sleep(2)
    # 返还前端图像路径信息
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
