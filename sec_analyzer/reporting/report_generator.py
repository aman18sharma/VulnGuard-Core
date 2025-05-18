# File: sec_analyzer/reporting/report_generator.py
from fpdf import FPDF
from datetime import datetime

class PDFReportGenerator(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "AegisAI Security Report", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

    def add_summary(self, findings: List[Dict]):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Executive Summary", 0, 1)
        self.ln(5)

        self.set_font("Arial", "", 12)
        self.multi_cell(0, 6,
            f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
            f"Total vulnerabilities found: {len(findings)}\n"
            f"Critical findings: {sum(1 for f in findings if f['risk_level'] == 'Critical')}"
        )

    def add_findings(self, findings: List[Dict]):
        self.add_page()
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Detailed Findings", 0, 1)
        self.ln(5)

        for idx, finding in enumerate(findings, 1):
            self.set_font("Arial", "B", 12)
            self.cell(0, 6, f"Finding #{idx}: {finding['vulnerability']}", 0, 1)
            self.set_font("Arial", "", 10)
            self.multi_cell(0, 6,
                f"File: {finding['file']}\n"
                f"Line: {finding['line']}\n"
                f"Risk Level: {finding.get('risk_level', 'Unknown')}\n"
                f"Recommendation: {finding.get('recommendation', 'No AI suggestion')}"
            )
            self.ln(3)

def generate_report(findings: List[Dict], output_path: str = None):
    report = PDFReportGenerator()
    report.add_summary(findings)
    report.add_findings(findings)

    if not output_path:
        output_path = f"security_report_{datetime.now().strftime('%Y%m%d%H%M')}.pdf"

    report.output(output_path)
    return output_path