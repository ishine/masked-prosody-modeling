from dataclasses import dataclass


@dataclass
class TrainingArgs:
    lr: float = 1e-4
    lr_schedule: str = "linear_with_warmup"
    lr_warmup_steps: int = 1000
    gradient_clip_val: float = 1.0
    checkpoint_path: str = "checkpoints"
    output_path: str = "outputs"
    run_name: str = None
    wandb_mode: str = "offline"
    wandb_project: str = None
    wandb_dir: str = "wandb"
    train_split: str = "train"
    val_split: str = "dev"
    n_steps: int = 50000
    batch_size: int = 32
    seed: int = 0
    dataset: str = "cdminix/libritts-aligned"
    log_every_n_steps: int = 100
    do_full_eval: bool = True
    do_save: bool = False
    save_onnx: bool = False
    eval_only: bool = False
    eval_every_n_steps: int = 1000
    save_every_n_steps: int = 1000
    push_to_hub: bool = False
    hub_repo: str = None


@dataclass
class CollatorArgs:
    overwrite: bool = False
    bin_size: int = 128
    mask_proportion: float = 0.5
    mask_proportion_tolerance: float = 0.05
    mask_length: int = 10
    max_length: int = 512
    vocex_model: str = "cdminix/vocex"
    name: str = "default"


@dataclass
class ModelArgs:
    n_layers: int = 8
    n_heads: int = 2
    kernel_size: int = 3
    filter_size: int = 256
    hidden_dim: int = 512
    dropout: float = 0.1
