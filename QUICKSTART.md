# Quick Start Guide

## First Time Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure credentials:**
   ```bash
   cp .env.example .env
   # Edit .env with your Bluesky credentials
   ```

3. **Test the bot:**
   ```bash
   python3 on_this_day_bot.py --demo
   ```

4. **Try a real post (optional):**
   ```bash
   python3 on_this_day_bot.py
   ```

## Scheduling Daily Posts

### Linux/macOS

```bash
./setup_cron.sh  # Shows the cron command
crontab -e       # Add the command to your crontab
```

### Windows

Use Task Scheduler:
- Program: `python.exe`
- Arguments: `on_this_day_bot.py`
- Start in: Path to this directory
- Trigger: Daily at 9:00 AM

## Troubleshooting

**No credentials?**
- Run with `--demo` flag to test without Bluesky account

**Can't access Wikipedia?**
- Bot automatically falls back to sample data

**Want different time?**
- Edit the cron schedule (first two numbers are minute and hour)

**Check logs:**
```bash
tail -f /tmp/bsky_bot.log
```

## Files

- `on_this_day_bot.py` - Main bot script
- `test_bot.py` - Test script
- `setup_cron.sh` - Cron setup helper
- `.env` - Your credentials (create from .env.example)
- `requirements.txt` - Python dependencies

## Commands

```bash
# Demo mode (no posting)
python3 on_this_day_bot.py --demo

# Post to Bluesky
python3 on_this_day_bot.py

# Test components
python3 test_bot.py

# Setup cron
./setup_cron.sh
```
