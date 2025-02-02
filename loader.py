import json
from pathlib import Path
from typing import Dict, Any

def read_json_file(filepath: str) -> Dict[str, Any]:
    """Read JSON file and return contents"""
    path = Path(filepath)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath}")
        
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {filepath}: {str(e)}")