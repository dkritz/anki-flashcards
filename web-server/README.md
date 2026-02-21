# Flashcard Web Server

A mobile-friendly flashcard web application for studying SQL and database concepts.

## Quick Start

### Start the Server

```bash
cd /home/dave/git/anki-flashcards/web-server
./start.sh
```

Or manually:

```bash
cd /home/dave/git/anki-flashcards/web-server
python3 server.py
```

## Access URLs

Once the server is running, access the flashcards at:

| URL | Description |
|-----|-------------|
| http://localhost:8080 | Local access |
| http://127.0.0.1:8080 | Local access (IP) |
| http://192.168.x.x:8080 | Network access (your local IP) |
| http://100.x.x.x:8080 | Tailscale/VPN access (if connected) |

## Features

- **Flip Cards**: Tap or click the card to reveal the answer
- **Swipe Navigation**: Swipe left/right to move between cards
- **Progress Bar**: Visual indicator of your progress through the deck
- **Deck Selector**: Choose from multiple study decks
- **Mobile Optimized**: Responsive design works on all devices
- **Keyboard Support**: Use arrow keys to navigate, Space/Enter to flip

## Available Decks

1. **SQL Data Engineering** - ETL/ELT, data warehousing, dimensional modeling
2. **SQL Server DBA** - Administration, backups, high availability
3. **T-SQL Keys** - Primary keys, foreign keys, constraints

## Adding New Decks

To add a new deck, edit `index.html` and add your cards to the `decks` object in the JavaScript:

```javascript
const decks = {
    // ... existing decks ...
    
    'my-new-deck': [
        { question: 'What is...?', answer: 'It is...' },
        { question: 'How do you...?', answer: 'You can...' }
    ]
};
```

Then add the deck to the dropdown selector:

```html
<select class="deck-selector" id="deckSelector">
    <!-- ... existing options ... -->
    <option value="my-new-deck">My New Deck</option>
</select>
```

### Card Format

Cards support basic Markdown formatting:

- `**bold text**` - Bold text
- `*italic text*` - Italic text
- `` `code` `` - Inline code

## Troubleshooting

### Port 8080 Already in Use

The `start.sh` script will automatically kill any existing process on port 8080. If it fails:

```bash
# Find the process using port 8080
lsof -ti:8080

# Kill it manually
kill -9 <PID>
```

### Permission Denied

Make scripts executable:

```bash
chmod +x start.sh
chmod +x server.py
```

### Cannot Access from Other Devices

1. Check your firewall settings
2. Ensure the server is binding to 0.0.0.0 (it does by default)
3. Verify you're using the correct IP address: `ip addr show`

### Server Not Starting

1. Check Python 3 is installed: `python3 --version`
2. Verify you're in the correct directory
3. Check file permissions

## File Structure

```
web-server/
├── index.html    # Main web application
├── server.py     # Python HTTP server
├── start.sh      # Startup script
└── README.md     # This file
```

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Requirements

- Python 3.x
- Modern web browser
- Optional: Tailscale (for VPN access)
