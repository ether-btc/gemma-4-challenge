# Gemma 4 Ethics Auditor

A pure-AI ethical code analysis tool built with Gemma 4, running locally on Raspberry Pi 5.

## Features
- **Ethical Analysis**: Uses Gemma 4 to analyze code for bias, accessibility, security, and ethics concerns
- **Hierarchical Analysis**: Handles large codebases by analyzing at file, function, and line levels
- **Local Execution**: Runs entirely on-device with no cloud API calls
- **Multiple Output Formats**: JSON and Markdown reports
- **Context Management**: Intelligent summarization to stay within 128K token window

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ether-btc/gemma-4-challenge.git
   cd gemma-4-challenge
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

## Usage

### Basic Commands

```bash
# Test Gemma 4 connection
python -m gemma_4_challenge.run_cli test

# Analyze a single file
python -m gemma_4_challenge.run_cli analyze /path/to/file.py --dimension bias

# Analyze a directory hierarchically
python -m gemma_4_challenge.run_cli analyze-directory /path/to/project --dimension bias --format json
```

### Options

- `--dimension`: Type of analysis (bias, accessibility, security, ethics)
- `--format`: Output format (json or markdown)
- `-d`: Short flag for --dimension
- `-f`: Short flag for --format

## How It Works

Gemma 4 loads locally via llama-cpp-python and analyzes code using carefully crafted prompts. For large files, the tool splits code into manageable chunks, summarizes where necessary, and maintains context to stay within token limits.

## Contest Alignment

This project meets the Gemma 4 Challenge requirements:
- Gemma 4 performs the core ethical analysis (real work)
- Runs locally on Raspberry Pi 5 (free, no credit card)
- Useful and creative tool for developers
- Can be extended to IoT, multimodal, or long-context applications

## Future Enhancements

- VS Code extension integration
- Git pre-commit hooks
- Real-time code editor analysis
- Confidence scoring and uncertainty reporting
- Support for additional programming languages