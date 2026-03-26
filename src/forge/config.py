from pydantic import BaseModel
import yaml
from pathlib import Path

class LLMConfig(BaseModel):
    provider: str = "anthropic"
    model: str = "claude-4-sonnet"
    api_key: str | None = None

class Config(BaseModel):
    llm: LLMConfig = LLMConfig()
    github_token: str | None = None

def load_config() -> Config:
    config_dir = Path.home() / ".config" / "forge"
    config_dir.mkdir(parents=True, exist_ok=True)
    config_path = config_dir / "config.yaml"

    if config_path.exists():
        with open(config_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        return Config.model_validate(data)

    # Create default config
    cfg = Config()
    with open(config_path, "w", encoding="utf-8") as f:
        yaml.dump(cfg.model_dump(), f, sort_keys=False)
    print(f"✅ Default config created at: {config_path}")
    return cfg