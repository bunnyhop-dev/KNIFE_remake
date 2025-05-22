import json
from pathlib import Path
from typing import Dict, Any

class Config:
    def __init__(self, config_file: str = "config.json"):
        self.config_file = Path(config_file)
        self.config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from file"""
        if self.config_file.exists():
            with open(self.config_file) as f:
                return json.load(f)
        return self._create_default_config()

    def _create_default_config(self) -> Dict[str, Any]:
        """Create default configuration"""
        config = {
                'scan_timeout': 30,
                'default_ports': '1-1000',
                'log_file': 'scanner.log',
                'output dir': 'scan_results'
                }
        self.save(config)
        return config

    def save(self, config: Dict[str, Any] = None):
        """Save configuration to file"""
        if config is not None:
            self.config = config
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value"""
        return self.config.get(key, default)

    def set(self, key: str, value: Any):
        """Set configuration value"""
        self.config[key] = value
        self.save()
