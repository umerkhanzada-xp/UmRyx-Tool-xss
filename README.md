# UmRyx-XSS-Tool

## 🚀 Overview

**UmRyx-XSS-Tool** is a fast and efficient XSS vulnerability scanner designed specifically for bug bounty hunters, penetration testers, and security researchers. This tool automates reconnaissance and XSS vulnerability testing across multiple target URLs, providing detailed vulnerability reports in both HTML and text formats.

---

## 🔧 Features

- 🔍 **Automated Reconnaissance**: Collects and tests URLs using reconnaissance tools such as `gau`, `gf`, `uro`, `Gxss`, and `kxss`.
- 🕵️‍♂️ **Fast XSS Testing**: Scans URLs for reflected XSS vulnerabilities using custom payloads.
- 💥 **Color-Coded HTML Reports**: Vulnerable and non-vulnerable URLs are displayed in a styled HTML page with animations and color coding.
- 🖼️ **Customizable Banner & Footer**: Add your custom banner, footer, and GitHub link with full support for logos and animations.
- 🎨 **Dynamic Themes**: Customize the look and feel of the HTML reports with background images and text colors.

---

## 🛠️ Installation

### Prerequisites

Before using the tool, ensure you have the following dependencies installed:

1. `Python 3`
2. `pip`
3. `figlet`
4. `gau`, `gf`, `uro`, `Gxss`, `kxss` (Install via `go get` or your package manager)
5. `curl` or `wget` for fetching URL data.

### Install Dependencies

```bash
pip install -r requirements.txt

📋 Usage
1. **Clone the repository**:

```bash
git clone https://github.com/umerkhanzada-xp/UmRyx-Tool-xss
cd UmRyx-XSS-Tool
bash umryx.sh

## 📝 Report Generation

- The tool will generate a report in both **HTML** and **Text** formats, displaying:
  - The list of vulnerable and non-vulnerable URLs.
  - A live update of vulnerability status during testing.

- HTML report includes:
  - A dynamic background.
  - Color-coded entries (Green for vulnerable, Red for non-vulnerable).
  - An animated footer displaying your GitHub link and other information.

---

## 🧰 Example

```bash
[+] Running automated reconnaissance...
[+] Scanning https://example.com for XSS vulnerabilities...
[+] Payload used: "<script>alert('hacked by Umer')</script>"
[+] Vulnerable: https://example.com/page?id=<script>alert('hacked by Umer')</script>


💻 Contributing
Feel free to open issues or contribute to the development of UmRyx-XSS-Tool by submitting pull requests.

Fork this repository
Clone your forked repository
Create a new branch (git checkout -b feature-xyz)
Make your changes and commit them (git commit -am 'Add new feature')
Push to your branch (git push origin feature-xyz)
Open a pull request

🖥️ License
This project is licensed under the MIT License - see the LICENSE file for details.

✨ Thank You
Developed with 💖 by Umer Khanzada.
Follow me on GitHub: @umerkhanzada-xp
