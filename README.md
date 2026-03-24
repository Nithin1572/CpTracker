# 🏆 CpTracker — Automated Codeforces Rating Scraper & Reporter

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Selenium](https://img.shields.io/badge/Selenium-4.x-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://selenium.dev)
[![Pandas](https://img.shields.io/badge/Pandas-1.3%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Chrome](https://img.shields.io/badge/ChromeDriver-Latest-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://chromedriver.chromium.org)
[![Excel](https://img.shields.io/badge/Excel%20I%2FO-openpyxl-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)](https://openpyxl.readthedocs.io)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

**A browser-automation pipeline that bulk-fetches Codeforces ratings for any number of users from a spreadsheet input — and exports a clean, structured report in seconds.**

[📁 Repository](https://github.com/Nithin1572/CpTracker) · [🐛 Issues](https://github.com/Nithin1572/CpTracker/issues)

</div>

---

**CpTracker** automates the entire workflow: supply an Excel file with usernames, and the system autonomously drives a headless browser to query each profile on [codeforces.com](https://codeforces.com), extracts the current rating, handles invalid/inactive users gracefully, and writes a ranked output spreadsheet — all without touching a single webpage manually.

---

## ✨ Key Features

| Feature | Details |
|---|---|
| **Bulk Processing** | Scrape ratings for an arbitrary number of users from a single Excel file |
| **Fault-Tolerant** | Invalid or non-existent usernames are caught via `try/except` and flagged — pipeline never crashes mid-run |
| **Structured I/O** | Accepts `.xlsx` input; emits a clean `.xlsx` report with username–rating pairs |
| **Headless-Ready** | `--headless` flag available in ChromeOptions for server/CI execution |
| **Flask Integration** | Web server scaffold included for future UI layer |
| **Zero Manual Steps** | One command to run; no web interaction required |

---

## 📂 Repository Structure

```
CpTracker/
│
├── main.py             # Core automation script (Selenium + Pandas pipeline)
├── input_list.xlsx     # Input: one Codeforces username per row (Column A)
├── output_list.xlsx    # Output: generated username–rating report
└── README.md
```

---

## ⚙️ Prerequisites

- Python **3.8+**
- Google Chrome browser installed
- ChromeDriver matching your Chrome version — [download here](https://chromedriver.chromium.org/downloads)
- ChromeDriver binary on your system `PATH`

---

## 🚀 Installation & Usage

**1. Clone the repository**
```bash
git clone https://github.com/Nithin1572/CpTracker.git
cd CpTracker
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
# Linux / macOS
source venv/bin/activate
# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install selenium pandas openpyxl flask
```

**4. Prepare your input file**

Open `input_list.xlsx` and add Codeforces usernames — one per row in **Column A**:

| A |
|---|
| tourist |
| Petr |
| Um_nik |
| your_username |

**5. Update the file path in `main.py`**

On line 11, replace the hardcoded path with a relative reference:
```python
# Before
df = pd.read_excel(r"C:\Users\Nithin\Desktop\CpTracker\input_list.xlsx")

# After (portable)
df = pd.read_excel("input_list.xlsx")
```

**6. Run the scraper**
```bash
python main.py
```

The script will open Chrome, iterate over each username, and write results to `output_list.xlsx` in the project directory.

<details>
<summary>📋 Sample Console Output (click to expand)</summary>

```
user name: ['tourist']   rating: Legendary Grandmaster
user name: ['Petr']      rating: International Grandmaster
user name: ['bad_user']  rating: INVALID USER
user name: ['Um_nik']    rating: Legendary Grandmaster

Output saved to output_list.xlsx
```

</details>

---

### Running in Headless Mode (no browser window)

To suppress the browser window (e.g. for server or CI execution), uncomment line 18 in `main.py`:

```python
options.add_argument("--headless")
```

---

## 📊 Output Format

`output_list.xlsx` is structured as follows:

| Username | Rating |
|---|---|
| tourist | Legendary Grandmaster |
| Petr | International Grandmaster |
| bad_user | INVALID USER |
| Um_nik | Legendary Grandmaster |

---

## 🔬 Technical Notes

### XPATH Selectors

The scraper targets Codeforces profile elements via XPATH. If Codeforces updates their DOM structure, these selectors may need to be updated:

```python
# Search input field
'//\*[@id="sidebar"]/div[4]/form/div[1]/label/input'

# Rating display span
'//\*[@id="pageContent"]/div[2]/div/div[2]/ul/li[1]/span[1]'
```

### Exception Handling Strategy

The pipeline uses a `try/except Exception` block to catch any DOM lookup failure (user not found, page structure change, network timeout). Rather than halting, it writes `"INVALID USER"` and continues — ensuring a complete report is always produced.

---

## ⚠️ Disclaimer

This tool interacts with the publicly accessible [codeforces.com](https://codeforces.com) website. Use responsibly — avoid high-frequency scraping that could place unnecessary load on their servers. For large-scale or production use, consider the [official Codeforces API](https://codeforces.com/apiHelp) instead.

---

## 📬 Contact

**Nithin Kumar Reddy Annapu Reddy**  
University of Illinois Springfield · MS Computer Science

[![LinkedIn](https://img.shields.io/badge/LinkedIn-nithinkrar-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/nithinkrar/)
[![GitHub](https://img.shields.io/badge/GitHub-Nithin1572-181717?style=flat&logo=github)](https://github.com/Nithin1572)

---

## 📄 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">
<sub>Built with ❤️ using <a href="https://selenium.dev">Selenium</a> · <a href="https://pandas.pydata.org">Pandas</a> · <a href="https://flask.palletsprojects.com">Flask</a></sub>
</div>
