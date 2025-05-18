# File: sec_analyzer/utils/config_manager.py
import yaml
import json
from pathlib import Path
from typing import Dict, Any

def load_config(config_path: str = None) -> Dict[str, Any]:
    default_path = Path(__file__).parent.parent / "config" / "default_config.yaml"
    with open(default_path) as f:
        config = yaml.safe_load(f)

    if config_path:
        with open(config_path) as f:
            custom_config = yaml.safe_load(f)
            config.update(custom_config)

    return config

def load_owasp_mappings() -> Dict[str, str]:
    path = Path(__file__).parent.parent / "config" / "owasp_mappings.json"
    with open(path) as f:
        return json.load(f)