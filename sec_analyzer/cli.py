# File: sec_analyzer/cli.py
import argparse
from pathlib import Path
from analysis.static_analyzer import StaticCodeAnalyzer
import RuntimeCodeAnalyzer
import AISecurityAssistant
import generate_report

def main():
    parser = argparse.ArgumentParser(description="AegisAI Code Security Analyzer")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Static analysis command
    static_parser = subparsers.add_parser("static", help="Analyze source code")
    static_parser.add_argument("path", help="Path to directory or file")

    # Runtime analysis command
    runtime_parser = subparsers.add_parser("runtime", help="Analyze runtime logs")
    runtime_parser.add_argument("path", help="Path to log directory or file")

    args = parser.parse_args()

    if args.command == "static":
        analyzer = StaticCodeAnalyzer()
        findings = analyzer.analyze(args.path)
    elif args.command == "runtime":
        analyzer = RuntimeCodeAnalyzer()
        findings = analyzer.analyze(args.path)

    # Enhance findings with AI
    ai = AISecurityAssistant()
    enhanced_findings = []
    for finding in findings:
        assessment = ai.assess_risk(finding)
        enhanced_findings.append({**finding, **assessment})

    # Generate report
    report_path = generate_report(enhanced_findings)
    print(f"Report generated: {report_path}")

if __name__ == "__main__":
    main()