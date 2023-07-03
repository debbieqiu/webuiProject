from webui import api_init

api = api_init.api


def get_img(optimize, lora, negative, seed, sampling, steps, height, width):
    result1 = api.txt2img(prompt="cute squirrel",
                          negative_prompt="ugly, out of frame",
                          seed=1003,
                          styles=["anime"],
                          cfg_scale=7,
                          #                      sampler_index='DDIM',
                          #                      steps=30,
                          #                      enable_hr=True,
                          #                      hr_scale=2,
                          #                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
                          #                      hr_second_pass_steps=20,
                          #                      hr_resize_x=1536,
                          #                      hr_resize_y=1024,
                          #                      denoising_strength=0.4,

                          )
    # result1 = api.txt2img(prompt=optimize + lora,
    #                       negative_prompt=negative,
    #                       seed=seed,
    #                       styles=["anime"],
    #                       cfg_scale=7,
    #                       sampler_name=sampling,
    #                       steps=steps,
    #                       #                      enable_hr=True,
    #                       #                      hr_scale=2,
    #                       #                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
    #                       #                      hr_second_pass_steps=20,
    #                       height=height,
    #                       width=width,
    #                       #                      denoising_strength=0.4,
    #                       )
    return result1
