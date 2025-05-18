# File: sec_analyzer/ai/assistant.py
import ollama
import json
from typing import Dict, List

class AISecurityAssistant:
    def __init__(self, model: str = "llama3"):
        self.model = model
        self.base_prompt = """Analyze this security vulnerability finding considering:
        - OWASP Top 10 2021 guidelines
        - Potential exploit impact
        - Common remediation strategies
        - Context from code snippet
        """

    def assess_risk(self, finding: Dict) -> Dict:
        prompt = f"{self.base_prompt}\n\nFinding Details:\n{json.dumps(finding, indent=2)}"

        try:
            response = ollama.chat(
                model=self.model,
                messages=[{"role": "user", "content": prompt}],
                format="json"
            )
            return json.loads(response['message']['content'])
        except Exception as e:
            return {
                "risk_level": "High",
                "recommendation": f"AI assessment failed: {str(e)}",
                "confidence": 0.0
            }

    def generate_report(self, findings: List[Dict]) -> str:
        summary = {
            "total_findings": len(findings),
            "critical": sum(1 for f in findings if f.get('risk_level') == "Critical"),
            "high_risk": sum(1 for f in findings if f.get('risk_level') == "High")
        }

        prompt = f"""Generate comprehensive security report with:
        1. Executive summary
        2. Risk distribution
        3. Critical vulnerabilities
        4. Remediation roadmap

        Data: {json.dumps(summary)}
        Findings: {json.dumps(findings[:5])}"""

        response = ollama.chat(
            model=self.model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response['message']['content']