# Anki Flashcards Web Server

A mobile-friendly web interface for studying Anki flashcards on your phone via Tailscale.

## 🚀 Quick Start

### Start the server manually:
```bash
cd ~/git/anki-flashcards/web-server
python3 server.py
```

### Access from your phone:
1. Connect to Tailscale on your phone
2. Open browser and go to: `http://100.116.183.50:8080`
3. Select a deck and start studying!

## 📱 Features

- **Mobile-optimized** - Works great on phones
- **Flip cards** - Tap to see answer
- **Swipe navigation** - Swipe left/right to change cards
- **Progress tracking** - See your progress through each deck
- **Multiple decks** - Switch between different topics
- **No installation** - Works in any browser

## 📚 Available Decks

1. **SQL Data Engineering** - Data engineering & stored procedures
2. **SQL Server DBA** - Database administration topics
3. **T-SQL Keys** - Key concepts and patterns

## 🔧 Auto-start on boot

```bash
# Enable service to start automatically
systemctl --user enable anki-flashcards.service

# Start now
systemctl --user start anki-flashcards.service

# Check status
systemctl --user status anki-flashcards.service

# View logs
journalctl --user -u anki-flashcards.service -f
```

## 🌐 Access URLs

- **Local**: http://localhost:8080
- **Tailscale**: http://100.116.183.50:8080 (your Tailscale IP)
- **Network**: http://[your-mac-ip]:8080

## 🎮 Controls

### On Mobile:
- **Tap card** - Flip to show answer
- **Swipe left** - Next card
- **Swipe right** - Previous card

### On Desktop:
- **Click card** - Flip
- **Arrow keys** - Navigate
- **Space** - Flip / Next card

## 📝 Adding New Decks

1. Create a new text file in the appropriate subdirectory
2. Follow the format:
   ```
   **Question: What is...?**
   **Answer:** The answer here...
   
   ---
   
   **Question: Next question...**
   **Answer:** Another answer...
   ```
3. Edit `index.html` and add the deck to the `decks` object:
   ```javascript
   'new-deck': {
       name: 'New Deck Name',
       file: '../path/to/flashcards.txt'
   }
   ```
4. Restart the server

## 🔒 Security

- Only accessible via Tailscale VPN (not public internet)
- No authentication required (trusted network)
- Read-only access to flashcards

## 🐛 Troubleshooting

**Can't access from phone:**
- Check Tailscale is connected on both devices
- Verify server is running: `systemctl --user status anki-flashcards`
- Check firewall: `sudo ufw allow 8080/tcp`

**Decks not loading:**
- Check browser console for errors
- Verify file paths in `index.html`
- Ensure text files are in correct format

**Port already in use:**
- Kill existing process: `pkill -f "server.py"`
- Or change PORT in `server.py`

## 🎯 Tips for Studying

- Review cards daily for spaced repetition
- Mark difficult cards for extra review
- Use the app during commute or breaks
- Focus on understanding, not memorization
- Create your own cards for weak areas

## 🔄 Updates

To add new flashcards:
1. Add `.txt` files to the repository
2. Update deck list in `index.html`
3. Restart server: `systemctl --user restart anki-flashcards`

---

*Happy studying! 📚*
