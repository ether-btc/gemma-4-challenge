from pathlib import Path
from .gemma_client import load_client, GemmaClient
import json

class HierarchicalAnalyzer:
    """Analyzes code hierarchically with context management."""

    def __init__(self, client=None):
        self.client = client or load_client()
        self._summary_cache = {}
        self._analysis_prompt = self._build_analysis_prompt()

    def _build_analysis_prompt(self):
        """Build a prompt for ethical analysis."""
        return """You are an ethical code reviewer. Analyze the following code for {dimension} concerns.
Provide a structured response in JSON format with the following keys:
- "issues": list of specific issues found (with line references if possible)
- "severity": string (HIGH/MEDIUM/LOW)
- "recommendations": list of specific recommendations
- "confidence": number between 0 and 1

The code snippet is:
```{code}```

Be thorough and specific."""

    def analyze_directory(self, directory_path, dimension):
        directory = Path(directory_path)
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        code_files = list(directory.rglob("*.py"))
        results = []
        for file_path in code_files:
            try:
                code = file_path.read_text()
                # For large files, use hierarchical analysis
                if len(code) > 10000:  # arbitrary threshold for splitting
                    analysis = self._analyze_large_file(code, dimension)
                else:
                    analysis = self._analyze_code(code, dimension)
                results.append({"file": str(file_path), "analysis": analysis})
            except Exception as e:
                results.append({"file": str(file_path), "error": str(e)})

        return {"directory": directory_path, "results": results}

    def _analyze_code(self, code, dimension):
        """Analyze a code snippet for ethical concerns."""
        prompt = self._analysis_prompt.format(dimension=dimension, code=code)
        response = self.client.analyze(prompt, max_tokens=2048)
        return self._parse_analysis_response(response)

    def _analyze_large_file(self, code, dimension):
        """Analyze a large file hierarchically."""
        import re
        functions = re.split(r'def\s+\w+\(.*?\)\s*:', code)
        analyses = []
        for func in functions:
            func = func.strip()
            if func:
                analysis = self._analyze_code(func, dimension)
                analyses.append(analysis)
        return {"type": "hierarchical", "parts": analyses, "combined_confidence": sum(a.get("confidence", 0) for a in analyses) / len(analyses) if analyses else 0}

    def _get_summary(self, code):
        """Get a summary of the code using Gemma 4."""
        prompt = f"Summarize the following code in 3-5 bullet points:\n```{code}```"
        response = self.client.analyze(prompt, max_tokens=512)
        return response

    def _parse_analysis_response(self, response):
        """Parse Gemma 4's analysis response into structured data."""
        try:
            data = json.loads(response)
            return {
                "issues": data.get("issues", []),
                "confidence": float(data.get("confidence", 0.8)),
                "severity": data.get("severity", "MEDIUM"),
                "recommendations": data.get("recommendations", []),
                "raw_response": response
            }
        except json.JSONDecodeError:
            # Fallback: try to extract confidence from text
            import re
            confidence = 0.8
            if "confidence" in response.lower():
                match = re.search(r'confidence\s*:\s*([0-9.]+)', response)
                if match:
                    confidence = float(match.group(1))
            return {
                "issues": [],
                "confidence": confidence,
                "severity": "MEDIUM",
                "recommendations": [],
                "raw_response": response
            }