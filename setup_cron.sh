#!/bin/bash
# Helper script for setting up the On This Day bot as a cron job

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Python executable
PYTHON=$(which python3)

# Generate cron command
CRON_CMD="0 9 * * * cd $SCRIPT_DIR && $PYTHON on_this_day_bot.py >> /tmp/bsky_bot.log 2>&1"

echo "On This Day Bot - Cron Setup Helper"
echo "===================================="
echo ""
echo "This script will help you set up a daily cron job."
echo ""
echo "Current directory: $SCRIPT_DIR"
echo "Python executable: $PYTHON"
echo ""
echo "Suggested cron entry (runs daily at 9:00 AM):"
echo ""
echo "$CRON_CMD"
echo ""
echo "To add this to your crontab:"
echo "1. Run: crontab -e"
echo "2. Add the line above"
echo "3. Save and exit"
echo ""
echo "To view current crontab: crontab -l"
echo "To check bot logs: tail -f /tmp/bsky_bot.log"
echo ""
echo "Alternative: Copy and run this command to add it automatically:"
echo ""
echo "(crontab -l 2>/dev/null; echo \"$CRON_CMD\") | crontab -"
echo ""
