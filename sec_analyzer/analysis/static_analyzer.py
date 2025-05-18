# File: sec_analyzer/analysis/static_analyzer.py
import re
import ast
from pathlib import Path
from typing import List, Dict, Any
from ..utils.config_manager import load_config, load_owasp_mappings

class StaticCodeAnalyzer:
    def __init__(self):
        self.config = load_config()
        self.owasp_mapping = load_owasp_mappings()
        self.patterns = self._compile_patterns()

    def _compile_patterns(self):
        return {
            'credentials': re.compile(
                r"({})\s*=\s*[\"'].+?[\"']".format("|".join(
                    self.config['analysis']['static']['credential_patterns']
                )),
                re.IGNORECASE
            ),
            'sql': re.compile(
                r"({})".format("|".join(
                    self.config['analysis']['static']['sql_patterns']
                )),
                re.IGNORECASE
            )
        }

    def analyze(self, path: str) -> List[Dict[str, Any]]:
        findings = []
        path = Path(path)

        if path.is_dir():
            files = path.rglob("*.*")
        else:
            files = [path]

        for file in files:
            if file.suffix in self.config['analysis']['static']['file_extensions']:
                with open(file) as f:
                    content = f.read()
                    findings += self._analyze_content(content, file)

        return findings

    def _analyze_content(self, content: str, file_path: Path) -> List[Dict]:
        findings = []

        # Credential detection
        for match in self.patterns['credentials'].finditer(content):
            findings.append(self._create_finding(
                file_path, match.start(), "Hard-coded Credentials",
                "A02", "High", content
            ))

        # SQL detection
        for match in self.patterns['sql'].finditer(content):
            findings.append(self._create_finding(
                file_path, match.start(), "Hard-coded SQL",
                "A03", "High", content
            ))

        # Logging check
        if not re.search(r"import\s+logging", content):
            findings.append({
                "file": str(file_path),
                "vulnerability": "Lack of Logging",
                "owasp": "A09",
                "severity": "Medium",
                "line": 0
            })

        return findings

    def _create_finding(self, file_path, pos, vuln_type, owasp, severity, content):
        return {
            "file": str(file_path),
            "line": content.count('\n', 0, pos) + 1,
            "vulnerability": vuln_type,
            "owasp": owasp,
            "severity": severity,
            "code_snippet": content[max(0, pos-20):pos+20]
        }