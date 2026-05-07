#!/usr/bin/env python3
"""
Gemma 4 Ethics Auditor - Main Entry Point
Pure AI-native ethical code analysis tool.
"""
import os
import sys
from pathlib import Path

def main():
    """Main entry point"""
    print("=" * 60)
    print("🚀 Gemma 4 Ethics Auditor")
    print("=" * 60)
    print("Pure AI-native ethical code analysis tool")
    print(f"📍 Running on: {Path.home()}")
    print(f"💾 Project directory: ~/gemma-4-challenge")
    print("=" * 60)
    
    # Simple test to verify Gemma 4 can load
    try:
        from transformers import AutoModelForCausalLM, AutoTokenizer
        print("✅ Transformers library loaded successfully")
        
        # Test loading a small model (we'll replace with Gemma 4 later)
        print("📦 Attempting to load Gemma 4 model...")
        print("(This may take a few minutes on Pi 5)")
        
    except ImportError as e:
        print(f"❌ Error loading transformers: {e}")
        print("Please run: pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
