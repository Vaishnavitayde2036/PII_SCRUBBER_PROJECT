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
    git clone [https://github.com/Vaishnavitayde2036/PII_SCRUBBER_PROJECT.git](https://github.com/Vaishnavitayde2036/PII_SCRUBBER_PROJECT.git)
    cd PII_SCRUBBER_PROJECT
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

## 💻 Usage

To run the PII SCRUBBER, simply run the module from the root directory:

```bash
python -m src.main --input data/journals.jsonl --output data/scrubbed.jsonl
```
## 📂 Project Structure

```text
PII_SCRUBBER_PROJECT/
├── data/
│   ├── journals.jsonl       # Raw input data
│   └── scrubbed.jsonl       # Processed output (Generated)
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry point and I/O handling
│   ├── scrubber.py          # Core PII removal logic and Regex patterns
│   └── patterns.py          # (Optional) Extended pattern definitions
├── tests/
│   └── test_scrubber.py     # Pytest unit tests
├── .gitignore
├── README.md
└── requirements.txt
```
## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

