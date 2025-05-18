# 🛡️ VulnGaurd Core

**AI-Powered Static & Runtime Code Vulnerability Detection**
*Aligning with OWASP Top 10 Standards*

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OWASP](https://img.shields.io/badge/OWASP%20Top%2010-2021%20Compliant-orange)](https://owasp.org/www-project-top-ten/)

---

## 📜 Features

### **Static Code Analysis**
- 🔍 Detect hardcoded credentials (API keys, passwords)
- 🧩 Identify potential SQL injection vectors
- 🚨 Memory leak detection
- 📉 Validate logging practices
- 📂 Third-party dependency checks

### **Runtime Behavior Analysis**
- 📊 Log analysis (`.log`, `.csv`, `.json`, `.txt`)
- 🎯 SQL/Command injection detection
- 🔓 Insecure file access monitoring
- 🌐 Network request security auditing

### **AI Integration**
- 🤖 Ollama-powered risk assessment
- 📈 Context-aware vulnerability prioritization
- 📝 Automated remediation recommendations
- 📄 PDF report generation

---

## ⚙️ Installation

1. **Prerequisites**:
   - Python 3.8+
   - [Ollama](https://ollama.ai/) installed and running

```bash
# Clone repository
git clone https://github.com/your-org/VulnGuard-Core.git
cd VulnGuard-Core

# Install dependencies
pip install -r requirements.txt

# Download AI model
ollama pull llama3