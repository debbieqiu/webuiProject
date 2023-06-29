import api_init

api = api_init.api


def txt2img(optimize, lora, negative, seed, sampling, steps, height, width):
    result1 = api.txt2img(prompt=optimize + lora,
                          negative_prompt=negative,
                          seed=seed,
                          styles=["anime"],
                          cfg_scale=7,
                          sampler_name=sampling,
                          steps=steps,
                          #                      enable_hr=True,
                          #                      hr_scale=2,
                          #                      hr_upscaler=webuiapi.HiResUpscaler.Latent,
                          #                      hr_second_pass_steps=20,
                          height=height,
                          width=width,
                          #                      denoising_strength=0.4,
                          )
    return result1
