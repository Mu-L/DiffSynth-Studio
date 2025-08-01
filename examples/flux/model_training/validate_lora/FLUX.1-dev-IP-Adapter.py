import torch
from diffsynth.pipelines.flux_image_new import FluxImagePipeline, ModelConfig
from PIL import Image


pipe = FluxImagePipeline.from_pretrained(
    torch_dtype=torch.bfloat16,
    device="cuda",
    model_configs=[
        ModelConfig(model_id="black-forest-labs/FLUX.1-dev", origin_file_pattern="flux1-dev.safetensors"),
        ModelConfig(model_id="black-forest-labs/FLUX.1-dev", origin_file_pattern="text_encoder/model.safetensors"),
        ModelConfig(model_id="black-forest-labs/FLUX.1-dev", origin_file_pattern="text_encoder_2/"),
        ModelConfig(model_id="black-forest-labs/FLUX.1-dev", origin_file_pattern="ae.safetensors"),
        ModelConfig(model_id="InstantX/FLUX.1-dev-IP-Adapter", origin_file_pattern="ip-adapter.bin"),
        ModelConfig(model_id="google/siglip-so400m-patch14-384"),
    ],
)
pipe.load_lora(pipe.dit, "models/train/FLUX.1-dev-IP-Adapter_lora/epoch-4.safetensors", alpha=1)

image = pipe(
    prompt="dog,white and brown dog, sitting on wall, under pink flowers",
    ipadapter_images=Image.open("data/example_image_dataset/1.jpg"),
    height=768, width=768,
    seed=0
)
image.save("image_FLUX.1-dev-IP-Adapter_lora.jpg")
