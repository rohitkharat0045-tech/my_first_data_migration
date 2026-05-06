#!/bin/bash

# Color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

# Banner function
function banner() {
    echo -e "${YELLOW}"
    echo "========================================"
    echo " 🚀 AUTOMATED DATABASE MIGRATION SYSTEM"
    echo "----------------------------------------"
    echo " Fast | Reliable | Cross-Platform"
    echo "========================================"
    echo -e "${NC}"
}

banner


if [ ! -d "venv" ]; then
    echo "⚙️ Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists."
fi

# ==============================================================

echo -e "${NC}"
echo -e "${GREEN}Select Environment:${NC}"
echo "1) Windows"
echo "2) Linux/Mac"
echo -e "${NC}"

read -p "Enter your choice (1 or 2): " choice

if [ "$choice" -eq 1 ]; then
    echo -e "${GREEN}Activating Windows virtual environment...${NC}"
    source venv/Scripts/activate

elif [ "$choice" -eq 2 ]; then
    echo -e "${GREEN}Activating Linux/Mac virtual environment...${NC}"
    source venv/bin/activate

else
    echo -e "${RED}❌ Invalid choice. Please enter 1 or 2.${NC}"
    exit 1   # 🔴 Stops entire script here
fi
echo -e "${NC}"

# ==============================================================

echo -e "${GREEN}Install Dependencies...${NC}"
pip install -r requirements.txt
echo -e "${NC}"

# ==============================================================

cd src

# ==============================================================
# 🚀 Run your actual process here (example)
echo -e "${GREEN}Running migration...${NC}"

run_with_progress() {
    echo "Running: $*"

    # Run passed command in background
    "$@" &
    PID=$!

    bar_length=20

    while kill -0 $PID 2>/dev/null
    do
        for ((i=0; i<=bar_length; i++))
        do
            filled=$(printf "%${i}s" | tr ' ' '#')
            empty=$(printf "%$((bar_length - i))s" | tr ' ' '.')

            printf "\rLoading... [%s%s]" "$filled" "$empty"
            sleep 0.2

            if ! kill -0 $PID 2>/dev/null; then
                break
            fi
        done
    done

    wait $PID
    status=$?

    printf "\rLoading... [####################]\n"

    if [ $status -eq 0 ]; then
        echo -e "${GREEN}✅ Execution completed successfully!${NC}"
    else
        echo -e "${RED}❌ Execution failed!${NC}"
    fi
}

# run_with_progress sleep 5
run_with_progress python3 migrate.py

# ==============================================================

cd ..

# ==============================================================
read -p "$(echo -e "${YELLOW}Do you want to view the report? (y/n): ${NC}")" confirm

if [[ "$confirm" == "y" || "$confirm" == "Y" ]]; then
    echo -e "${GREEN}📄 Showing report...${NC}"
    cat reports/report.txt
elif [[ "$confirm" == "n" || "$confirm" == "N" ]]; then
    echo -e "${GREEN}skipping report...${NC}"
else
    echo -e "${RED}❌ Invalid input! Please enter y or n.${NC}"
    exit 1
fi
