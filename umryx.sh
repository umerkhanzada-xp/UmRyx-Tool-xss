#!/bin/bash

# ┌────────────────────────────────────────────┐
# │ UmRyx - Fast Recon Bug Bounty Tool         │
# │ Author: Umer Khanzada (a.k.a Ryx)          │
# └────────────────────────────────────────────┘

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m' # No Color

# Required tools check
required_tools=("figlet" "gau" "gf" "uro" "Gxss" "kxss" "python3")
for tool in "${required_tools[@]}"; do
    if ! command -v $tool &> /dev/null; then
        echo -e "${RED}[✘] $tool is not installed. Please install it to use this tool.${NC}"
        exit 1
    fi
done

# Clear screen & show banner
clear
figlet -c "Um-Ryx" | lolcat
echo -e "${CYAN}==============================================${NC}"
echo -e "${BOLD}     Developed by: ${GREEN}Umer Khanzada a.k.a Ryx${NC}"
echo -e "${CYAN}==============================================${NC}"

# Greeting
echo -e "${YELLOW}[+] Welcome to ${CYAN}UmRyx${YELLOW}, your automated recon assistant!${NC}"
echo -e "${YELLOW}[+] Let's begin the reconnaissance journey... 🚀${NC}"

# Ask for target
echo -ne "${CYAN}[?]${NC} Enter target domain: "
read target_domain

# Loading animation
echo -ne "${YELLOW}[+] Initializing"
for i in {1..5}; do echo -n "."; sleep 0.3; done
echo -e " ${GREEN}Done!${NC}\n"

# Methodology chain
echo -e "${CYAN}[⚙️] Running recon on: ${target_domain}${NC}"
echo -e "${YELLOW}[~] Gathering URLs, filtering with gf patterns, deduplicating, and scanning with Gxss/Kxss...${NC}\n"

echo $target_domain | gau | gf xss | uro | Gxss | kxss | tee xss_output.txt

# Post-process
echo -ne "${YELLOW}[+] Processing results"
for i in {1..3}; do echo -n "."; sleep 0.3; done
echo -e " ${GREEN}Done!${NC}"

# Extract final URLs
cat xss_output.txt | grep -oP '^URL: \K\S+' | sed 's/=.*/=/' | sort -u > final.txt

# Result check
if [[ -f "final.txt" ]]; then
    echo -e "${GREEN}[✓] final.txt successfully saved in the current directory.${NC}"
else
    echo -e "${RED}[✘] Failed to generate final.txt${NC}"
    exit 1
fi

# Done message
echo -e "\n${GREEN}[✔] Recon complete. Output saved to final.txt${NC}"
echo -e "${CYAN}[>] Launching custom XSS scanner with final results... 🔍${NC}"

# Run Python XSS scanner
python3 xss_scanner.py

