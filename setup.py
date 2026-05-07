#!/usr/bin/env python3
"""Setup script for Gemma 4 Ethics Auditor"""

import os
import sys
import subprocess
from pathlib import Path

def install_dependencies():
    deps = ["torch", "transformers", "accelerate", "safetensors", "rich", "typer"]
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", *deps])
    
def setup_environment():
    print("Setting up Gemma 4 Ethics Auditor environment...")
    (Path.home() / "gemma-4-challenge" / "models").mkdir(exist_ok=True)
    (Path.home() / "gemma-4-challenge" / "cache").mkdir(exist_ok=True)
    print("✅ Environment ready!")
    print("📁 Project directory: ~/gemma-4-challenge")

if __name__ == "__main__":
    install_dependencies()
    setup_environment()
