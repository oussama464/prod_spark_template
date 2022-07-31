from configparser import ConfigParser
from pathlib import Path
from typing import Dict, Optional


def get_configs(conf_path, section: str, name: Optional[str] = None):
    config = ConfigParser()
    config.read(conf_path)
    if name:
        return config[section][name]
    return {k: v for k, v in config[section].items()}
