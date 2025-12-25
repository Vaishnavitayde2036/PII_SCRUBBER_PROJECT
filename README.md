# PII Scrubber 🛡️

**PII Scrubber** is a robust Data Loss Prevention (DLP) tool designed to detect and redact Personally Identifiable Information (PII) from log files and datasets.

Designed for Cyber Security contexts, it utilizes a hybrid approach combining **Regular Expressions (Regex)** for rigid patterns (like IDs and dates) and **Natural Language Processing (Spacy NLP)** for context-aware entity recognition (like names and clinics).

## 🚀 Key Features

* **Hybrid Detection Engine:** Uses Regex for precision and AI (Spacy) for context.
* **Context-Aware Scrubbing:** Distinguishes between generic organizations and Medical Providers (`[PROVIDER]`).
* **Australian Localization:** Specialized support for Australian phone formats (`+61`) and dates (`DD/MM/YYYY`).
* **Smart Address Redaction:** Detects complex street addresses including suburbs and postcodes.
* **CLI Tool:** Efficient command-line interface for batch processing logs.

## 🛠️ Supported Redactions

The tool automatically replaces sensitive data with the following standardized tags:

| Type | Tag | Description |
| :--- | :--- | :--- |
| **Names** | `[NAME]` | Patient and Doctor names (e.g., "John Smith", "Dr. Rao") |
| **Providers** | `[PROVIDER]` | Clinics, Hospitals, and Healthcare organizations |
| **Contact** | `[EMAIL]`, `[PHONE]` | Email addresses and Australian mobile/landlines |
| **Location** | `[ADDRESS]` | Full street addresses, cities, and states |
| **Dates** | `[DOB]` | Dates of birth or appointment dates |
| **IDs** | `[APPT_ID]` | Reference numbers (e.g., `REF-12345`) |

## 📦 Installation

### Prerequisites
* Python 3.9 or higher
* `pip` package manager

### Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/pii-scrubber.git](https://github.com/yourusername/pii-scrubber.git)
    cd pii-scrubber
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Download the NLP Model:**
    ```bash
    python -m spacy download en_core_web_sm
    ```

## 💻 Usage

The project includes a convenient shortcut command `pii_scrub`.

**Basic Command:**
```powershell
.\pii_scrub --in data/input_file.jsonl --out data/output_file.jsonl