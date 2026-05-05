#!/bin/bash

# Color variables
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
MAGENTA='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color


# Banner function
function banner() {
    echo -e "${YELLOW}"
    echo "========================================"
    echo "   DATABASE MIGRATION TOOL 🚀"
    echo "========================================"
    echo -e "${NC}"
    echo -e "${CYAN}this is temp:${NC}"
    echo -e "${GREEN}this is test${NC}"
    echo -e "${YELLOW}──────────────────────────────────────────────${NC}"
}

# Display banner
banner

pwd
cd src
pwd

PID=$!

# Progress bar settings
bar_length=20

while kill -0 $PID 2>/dev/null
do
    for ((i=0; i<=bar_length; i++))
    do
        # build bar
        filled=$(printf "%${i}s" | tr ' ' '#')
        empty=$(printf "%$((bar_length - i))s" | tr ' ' '.')

        printf "\rLoading... [%s%s]" "$filled" "$empty"
        sleep 0.2

        # break if process finished
        if ! kill -0 $PID 2>/dev/null; then
            break
        fi
    done
done

wait $PID

# full bar at end
printf "\rLoading... [####################]\n"
echo "✅ Execution completed!"

pwd
cd ..
cat reports/report.txt