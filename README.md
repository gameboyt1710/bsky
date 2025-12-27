# On This Day Bluesky Bot 📅

An automated Bluesky bot that posts daily "On This Day" facts from Wikipedia, including historical events, births, and deaths.

## Features

- 📚 Fetches facts from Wikipedia's "On This Day" API
- 🎲 Posts a random historical event, birth, or death
- 🤖 Fully automated posting to Bluesky
- ⏰ Easy to schedule with cron or Task Scheduler
- 🔒 Secure credential management with environment variables

## Prerequisites

- Python 3.7 or higher
- A Bluesky account
- A Bluesky app password (see setup instructions below)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/gameboyt1710/bsky.git
cd bsky
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your credentials:
```bash
cp .env.example .env
```

4. Edit `.env` and add your Bluesky credentials:
```
BLUESKY_HANDLE=your-handle.bsky.social
BLUESKY_PASSWORD=your-app-password
```

## Getting a Bluesky App Password

1. Log in to your Bluesky account at https://bsky.app
2. Go to Settings → App Passwords
3. Click "Add App Password"
4. Give it a name (e.g., "On This Day Bot")
5. Copy the generated password to your `.env` file

**Important:** Use an app password, not your main account password!

## Usage

### Demo Mode (Testing Without Credentials)

You can test the bot without Bluesky credentials using demo mode:

```bash
python3 on_this_day_bot.py --demo
```

This will:
- Generate a random fact from sample data
- Display the formatted post
- Show the character count
- Exit without posting to Bluesky

Perfect for testing your setup before connecting to Bluesky!

### Manual Run

To post a single "On This Day" fact:

```bash
python3 on_this_day_bot.py
```

The script will:
1. Fetch a random fact from Wikipedia's "On This Day" API
2. Format it nicely for Bluesky
3. Post it to your account

**Note:** If Wikipedia API is unavailable, it will automatically fall back to sample data.

### Automated Daily Posts

#### Linux/macOS (using cron)

**Easy Setup:**

Run the helper script to get the cron command:
```bash
./setup_cron.sh
```

This will display the command you need to add to your crontab.

**Manual Setup:**

1. Open your crontab:
```bash
crontab -e
```

2. Add a line to run the bot daily at 9 AM:
```
0 9 * * * cd /path/to/bsky && /usr/bin/python3 on_this_day_bot.py >> /tmp/bsky_bot.log 2>&1
```

Replace `/path/to/bsky` with the actual path to your repository.

#### Windows (using Task Scheduler)

1. Open Task Scheduler
2. Create a new Basic Task
3. Set the trigger to "Daily" at your preferred time
4. Set the action to "Start a program"
5. Program: `python.exe`
6. Arguments: `on_this_day_bot.py`
7. Start in: Path to your repository

#### Using systemd timer (Linux)

Create a systemd service and timer for more control:

1. Create service file `/etc/systemd/system/bsky-bot.service`:
```ini
[Unit]
Description=On This Day Bluesky Bot
After=network.target

[Service]
Type=oneshot
User=yourusername
WorkingDirectory=/path/to/bsky
ExecStart=/usr/bin/python3 on_this_day_bot.py
StandardOutput=journal
StandardError=journal

[Install]
WantedBy=multi-user.target
```

2. Create timer file `/etc/systemd/system/bsky-bot.timer`:
```ini
[Unit]
Description=Run Bluesky Bot Daily
Requires=bsky-bot.service

[Timer]
OnCalendar=daily
OnCalendar=09:00
Persistent=true

[Install]
WantedBy=timers.target
```

3. Enable and start the timer:
```bash
sudo systemctl enable bsky-bot.timer
sudo systemctl start bsky-bot.timer
```

## How It Works

1. **Wikipedia API**: The bot uses Wikipedia's official REST API to fetch "On This Day" facts for the current date
2. **Fact Selection**: It randomly selects from historical events, births, or deaths
3. **Formatting**: Facts are formatted with appropriate emojis and structure
4. **Bluesky Posting**: Uses the AT Protocol client library to authenticate and post to Bluesky

## Example Posts

```
📅 On This Day in 1969:

Apollo 11 astronauts Neil Armstrong and Buzz Aldrin became the first humans to walk on the Moon.
```

```
🎂 Born On This Day in 1867:

Marie Curie, Polish-French physicist and chemist who conducted pioneering research on radioactivity.
```

```
🕊️ Died On This Day in 1965:

Winston Churchill, British Prime Minister during World War II and Nobel Prize winner in Literature.
```

## Troubleshooting

### "Error: BLUESKY_HANDLE and BLUESKY_PASSWORD must be set"
- Make sure you've created a `.env` file from `.env.example`
- Verify your credentials are properly set in the `.env` file

### "Error logging in"
- Verify your handle is correct (should include `.bsky.social`)
- Make sure you're using an app password, not your main password
- Check if your account is active and not suspended

### "Error fetching Wikipedia data"
- Check your internet connection
- Wikipedia API might be temporarily unavailable
- Try running the script again later

### "Failed to post to Bluesky"
- Check if you've exceeded rate limits
- Verify your account has posting permissions
- Check the error message for specific details

## Configuration

You can customize the bot by editing `on_this_day_bot.py`:

- Change the fact selection logic in `select_random_fact()`
- Modify formatting in `format_event()`, `format_birth()`, and `format_death()`
- Adjust the emoji or text structure to your preference

## Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## License

This project is open source and available under the MIT License.

## Disclaimer

This bot uses Wikipedia's API. Please review their [API terms of use](https://www.mediawiki.org/wiki/REST_API) and use responsibly. The bot identifies itself with a proper User-Agent header as recommended.

## Credits

- Wikipedia API for providing "On This Day" data
- AT Protocol Python SDK for Bluesky integration
- Built with ❤️ for the Bluesky community
