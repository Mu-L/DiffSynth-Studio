accelerate launch --config_file examples/flux/model_training/full/accelerate_config.yaml examples/flux/model_training/train.py \
  --dataset_base_path data/example_image_dataset \
  --dataset_metadata_path data/example_image_dataset/metadata.csv \
  --max_pixels 1048576 \
  --dataset_repeat 400 \
  --model_id_with_origin_paths "black-forest-labs/FLUX.1-Krea-dev:flux1-krea-dev.safetensors,black-forest-labs/FLUX.1-dev:text_encoder/model.safetensors,black-forest-labs/FLUX.1-dev:text_encoder_2/,black-forest-labs/FLUX.1-dev:ae.safetensors" \
  --learning_rate 1e-5 \
  --num_epochs 1 \
  --remove_prefix_in_ckpt "pipe.dit." \
  --output_path "./models/train/FLUX.1-Krea-dev_full" \
  --trainable_models "dit" \
  --use_gradient_checkpointing
