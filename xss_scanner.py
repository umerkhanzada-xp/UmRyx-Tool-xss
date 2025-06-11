import requests
import time
import sys

# Color codes
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Loading animation
def animate_loading(text):
    for _ in range(3):
        for dot in ['.', '..', '...']:
            sys.stdout.write(f'\r{text}{dot}')
            sys.stdout.flush()
            time.sleep(0.3)
    sys.stdout.write('\r')

# URL validator
def validate_url(url):
    return url.startswith('http://') or url.startswith('https://')

# Load payloads
def load_payloads():
    with open('payloads.txt', 'r') as f:
        return [p.strip() for p in f.readlines()]

# Load URLs
def load_urls():
    with open('final.txt', 'r') as f:
        return [u.strip() for u in f.readlines()]

# Generate HTML report
def generate_html_report(vulnerable_urls, non_vulnerable_urls, output_file="vulnerable_report.html"):
    with open(output_file, "w") as html:
        html.write("<html><head><title>UmRyx XSS Report</title><style>")
        html.write("""
        body {
            background: #000 url('https://wallpapercave.com/wp/wp1810653.jpg') no-repeat center center fixed;
            background-size: cover;
            font-family: 'Courier New', monospace;
            color: #fff;
        }
        h1, h2 { text-align: center; text-shadow: 0 0 10px red; }
        marquee { color: yellow; background: rgba(0,0,0,0.5); padding: 10px; font-size: 1.5em; }
        table { width: 100%; border-collapse: collapse; margin: 20px auto; }
        th, td { padding: 10px; border: 1px solid red; }
        th { background-color: #440000; color: yellow; }
        td.vulnerable { color: yellow; background: #550000; }
        td.non-vulnerable { color: red; background: #220000; }
        a { color: yellow; text-decoration: none; }
        """)
        html.write("</style></head><body>")
        html.write("<marquee>Developed by <a href='https://github.com/umerkhanzada-xp' target='_blank'>Umer Khanzada</a></marquee>")
        html.write("<h1>UmRyx XSS Report</h1><h2>Vulnerable URLs</h2><table><tr><th>#</th><th>URL</th></tr>")
        for i, url in enumerate(vulnerable_urls, 1):
            html.write(f"<tr><td>{i}</td><td class='vulnerable'><a href='{url}' target='_blank'>{url}</a></td></tr>")
        html.write("</table><h2>Non-Vulnerable URLs</h2><table><tr><th>#</th><th>URL</th></tr>")
        for i, url in enumerate(non_vulnerable_urls, 1):
            html.write(f"<tr><td>{i}</td><td class='non-vulnerable'><a href='{url}' target='_blank'>{url}</a></td></tr>")
        html.write("</table></body></html>")
    print(f"\n{CYAN}[✓] HTML report saved as: {output_file}{RESET}")

# Main XSS Scanner
def scan_xss():
    urls = load_urls()
    payloads = load_payloads()
    vulnerable_urls = []
    non_vulnerable_urls = []

    for url in urls:
        if not validate_url(url):
            print(f"{RED}[!] Skipping invalid URL: {url}{RESET}")
            non_vulnerable_urls.append(url)
            continue

        print(f"{YELLOW}[~] Scanning: {CYAN}{url}{RESET}")
        animate_loading("  Scanning")
        xss_hits = 0

        for payload in payloads:
            test_url = f"{url}{payload}"
            try:
                response = requests.get(test_url, timeout=4)
                if payload in response.text:
                    print(f"{GREEN}[+] XSS Detected: {test_url}{RESET}")
                    vulnerable_urls.append(test_url)
                    xss_hits += 1
                    if xss_hits >= 2:
                        print(f"{CYAN}[-] Found 2 XSS hits. Skipping remaining payloads for this URL.{RESET}")
                        break
                else:
                    print(f"{RED}[-] Not Vulnerable: {test_url}{RESET}")
            except requests.RequestException as e:
                print(f"{RED}[!] Error with {test_url} -> {e}{RESET}")
                break  # Break if connection fails to avoid timeout loop

        if xss_hits == 0:
            non_vulnerable_urls.append(url)

    generate_html_report(vulnerable_urls, non_vulnerable_urls)

# Entry Point
if __name__ == "__main__":
    scan_xss()
