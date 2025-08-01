# Segwise Dashboard QA Automation

This repository contains a QA testing solution for the Segwise AI Dashboard. It includes both **manual testing results** and an **automated Selenium test script** to validate key dashboard functionality.

---

## 📄 Project Summary

- 🔍 Identified and documented **12 functional/UX bugs**
- 🧪 Created **5 suggested test cases** to validate key workflows
- ✅ Wrote a **Selenium script** (`test_dashboard.py`) to automate login and chart verification
- 📋 Prepared a **regression checklist with 9 core components** (Google Sheet)

---

## 📂 File Structure

Segwise/
│
├── test_dashboard.py # Selenium automation script
├── README.md # Project summary and instructions
├── QA_Report.pdf # Manual bug report and test cases
├── regression_checklist.xlsx # Regression checklist (manual)


---

## ✅ Automation Script Details

**Script Name:** `test_dashboard.py`  
**Tools Used:** Python + Selenium

### What it Does:
- Opens Segwise login page
- Logs in using test credentials
- Waits for the dashboard to load
- Verifies the presence of a key dashboard chart using XPath


