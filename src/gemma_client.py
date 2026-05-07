"""
Gemma 4 Ethics Auditor - Gemma 4 Client Wrapper
Pure AI-native ethical code analysis tool.
"""
import os
from pathlib import Path
from llama_cpp import Llama


# Default model path on USB
DEFAULT_MODEL_PATH = "/mnt/usb/hermes/models/gemma-4-E2B-it-Q8_0.gguf"


class GemmaClient:
    """Wrapper for Gemma 4 GGUF model via llama-cpp-python."""

    def __init__(
        self,
        model_path: str = DEFAULT_MODEL_PATH,
        n_ctx: int = 4096,
        n_threads: int = 4,
        verbose: bool = False,
    ):
        """Initialize Gemma 4 client."""
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found: {model_path}")

        self.model_path = model_path
        self.llm = Llama(
            model_path=model_path,
            n_ctx=n_ctx,
            n_threads=n_threads,
            verbose=verbose,
        )
        print(f"✅ Gemma 4 loaded from {model_path}")

    def analyze(self, prompt: str, max_tokens: int = 2048) -> str:
        """Run inference with a prompt."""
        output = self.llm.create_chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
        )
        return output["choices"][0]["message"]["content"]

    def analyze_code(self, code: str, dimension: str = "bias") -> str:
        """Analyze code for ethical concerns.

        Args:
            code: Source code to analyze
            dimension: One of 'bias', 'accessibility', 'security', 'ethics'

        Returns:
            Analysis report from Gemma 4
        """
        system_prompts = {
            "bias": "You are an ethical code reviewer specializing in detecting bias "
                    "(gender, cultural, ability) in code and comments. Analyze the code "
                    "and identify potential bias issues with specific examples.",
            "accessibility": "You are an ethical code reviewer checking for WCAG accessibility "
                            "compliance. Analyze UI/UX code for accessibility barriers.",
            "security": "You are an ethical security reviewer analyzing data handling, "
                       "privacy implications, and secure coding practices.",
            "ethics": "You are an ethical code reviewer evaluating clarity, maintainability, "
                     "and technical debt ethics.",
        }

        prompt = f"""<bos><start_of_turn>user
Analyze this code for {dimension} concerns:

```{code}
```

Provide a structured report with:
1. Issues found (with line references if possible)
2. Severity: HIGH/MEDIUM/LOW
3. Specific recommendations

Be specific and actionable.<end_of_turn>
<start_of_turn>model
"""

        output = self.llm(
            prompt,
            max_tokens=2048,
            stop=["<end_of_turn>"],
        )
        return output["choices"][0]["text"]


def load_client() -> GemmaClient:
    """Load Gemma 4 client with default settings."""
    return GemmaClient()
