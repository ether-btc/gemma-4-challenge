# ETHICA - Gemma 4 Ethics Auditor

A pure-AI ethical code analysis tool built with Gemma 4, running locally on Raspberry Pi 5.

## Project Overview
**Project Name:** Ethica - Local AI Ethics & Bias Auditor  
**Challenge:** Gemma 4 Challenge  
**Category:** Build With Gemma 4  
**Hardware:** Raspberry Pi 5 (8GB) running Debian  
**Core Principle:** 100% Gemma 4-powered analysis — no external tools, no pre-written rules

## Architecture
- **Gemma 4 Inference Engine** (On-Device GGUF via llama-cpp-python)
- **Hierarchical Analyzer** (file → function → line level analysis)
- **CLI Interface** (typer + rich)
- **Report Generator** (JSON and Markdown output)

## 🎯 Problem Statement
Developers need privacy-preserving, cost-effective ethical analysis of code without sending sensitive data to cloud services. Existing solutions rely on cloud APIs or traditional static analysis tools.

## 💡 Unique Solution
Gemma 4 acts as the **sole ethics auditor** — reading code, identifying bias, accessibility issues, and ethical risks through pure reasoning, then generating actionable reports.

## 🏗️ Architecture

### Core Components
1. **Gemma 4 Inference Engine** (On-Device, quantized)
2. **Prompt Management System** (hierarchical prompts for different analysis dimensions)
3. **Code Input Handler** (stdin, file, directory support)
4. **Analysis Orchestrator** (manages multi-pass analysis for large codebases)
5. **Report Generator** (CLI, Markdown, JSON outputs)
6. **Integration Layer** (git hooks, IDE extensions)

### Analysis Dimensions
- **Bias Detection:** Gender, cultural, ability bias in code/comments
- **Accessibility:** WCAG compliance in UI/UX code
- **Security Ethics:** Data handling, privacy implications
- **Code Ethics:** Clarity, maintainability, technical debt ethics

## 📋 Implementation Plan

### Phase 1: Foundation (Week 1)
- [x] Set up Gemma 4 On-Device environment
- [x] Create core prompt templates for each analysis dimension
- [x] Build basic CLI interface
- [x] Implement code input handling

### Phase 2: Analysis Engine (Week 2)
- [ ] Hierarchical analysis for large codebases
- [ ] Confidence scoring system
- [ ] Context management for 128K token window
- [ ] Caching for repeated analyses

### Phase 3: Reporting & Integration (Week 3)
- [ ] Multiple output formats (CLI, Markdown, JSON)
- [ ] Git pre-commit hook integration
- [ ] VS Code extension prototype
- [ ] Performance optimizations for Pi 5

## ⚙️ Technical Specifications

### Model Configuration
- **Model:** Gemma 4 On-Device (quantized 4-bit/5-bit)
- **Context Window:** 128K tokens
- **Inference:** Local, no internet required
- **RAM Usage:** Optimized for 8GB Pi 5

### Prompt Design Philosophy
- Gemma 4 acts as "ethical code reviewer"
- Multi-step reasoning: read → analyze → evaluate → recommend
- Context-aware: considers code structure and intent
- Confidence-based: flags uncertain findings

## 🚦 Current Progress

### ✅ Completed (Week 1 Start)
- [x] Project scope and architecture defined
- [x] Challenge rules reviewed and compliance confirmed
- [x] Hardware constraints analyzed
- [x] Model selection rationale documented
- [x] Pure AI-native constraint established

### 🔄 In Progress
- Hierarchical analysis for large codebases (Phase 2)
- Building first prompt templates and CLI skeleton

## ⏭️ Next Immediate Steps

1. **Gemma 4 Environment Setup**
   - Install required dependencies
   - Load Gemma 4 On-Device model
   - Test basic inference

2. **First Prompt Implementation**
   - Create bias detection prompt template
   - Test on sample code snippets
   - Iterate based on results

3. **CLI Skeleton**
   - stdin/file input handling
   - Basic output formatting
   - Error handling

## 📁 File Structure
```
gemma-4-challenge/
├── ETHICA_AUDITOR_PROJECT.md  # This file
├── setup.sh                   # Environment setup script
├── requirements.txt           # Python dependencies
├── src/
│   ├── __init__.py
│   ├── gemma_client.py       # Gemma 4 inference wrapper
│   ├── prompts.py            # Prompt templates and management
│   ├── analyzer.py           # Analysis orchestration
│   ├── reporter.py           # Report generation
│   └── integrations/         # Git hooks, IDE extensions
├── tests/
│   ├── sample_code/          # Test code snippets
│   └── test_prompts.py       # Prompt testing
├── docs/
│   ├── architecture.md        # Technical documentation
│   └── ethical_frameworks.md  # Ethical guidelines used
└── demo/
    └── demo_video_script.md   # Video demonstration script
```

## 🎯 Success Metrics for Challenge

1. **Functionality (40%)**
   - Works on Pi 5 with 8GB RAM
   - Handles multiple programming languages
   - Produces actionable, accurate reports

2. **Educational Value (30%)**
   - Teaches developers about ethical coding
   - Explains reasoning clearly
   - Provides learning resources

3. **Technical Execution (20%)**
   - Clean, well-documented code
   - Efficient use of Gemma 4
   - Robust error handling

4. **Originality (10%)**
   - Pure AI-native approach
   - Unique application of Gemma 4
   - Solves a real problem creatively

## ⚠️ Important Notes

### Challenge Compliance
- **Category:** Build With Gemma 4 (not Write)
- **Submission:** Single project, no duplication
- **Rule Adherence:** 100% Gemma 4-powered analysis (no external tools)
- **Deadline:** May 24, 2025 (3 weeks from start)

### Hardware Constraints
- **No swap file** on SD card (ZRAM only)
- **8GB RAM** limits model size/quantization
- **SD card wear** — minimize writes, use caching

### Pure AI-native Enforcement
- No ESLint, Bandit, or other static analysis tools
- No pre-written rules or regex patterns
- All analysis performed by Gemma 4 reasoning
- Prompts are the primary code artifact

---

**Last saved:** May 7, 2025  
**Project lead:** [Your Name]  
**Next session start:** Continue from "Gemma 4 Environment Setup"