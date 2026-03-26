import yaml
from pathlib import Path
from jinja2 import Environment, BaseLoader
from .config import load_config

class Forge:
    def __init__(self):
        self.config = load_config()

    def load_prompt(self, name: str, **kwargs) -> str:
        prompt_path = Path(__file__).parent / "prompts" / f"{name}.yaml"
        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt '{name}' not found in prompts folder.")

        with open(prompt_path, encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}

        system = data.get("system", "")
        user = data.get("user", "")

        env = Environment(loader=BaseLoader())
        template = env.from_string(system + "\n\n" + user)
        return template.render(**kwargs)