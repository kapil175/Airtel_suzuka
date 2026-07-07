# Digital Clock - Multiple Time Zones

A beautiful, real-time digital clock that displays the current time across 7 different time zones around the world.

## Available Versions

### 1. Desktop App (Tkinter) - `room.py`
Traditional Python desktop application with dark-themed GUI.

**Run:**
```bash
pip install pytz
python room.py
```

### 2. Web App (Flask) - `app.py` ⭐ **RECOMMENDED**
Modern web-based clock accessible from any browser with live updates.

## Installation & Setup

### Requirements
- Python 3.6+
- pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually install:
```bash
pip install Flask pytz
```

### Step 2: Run the Web Application
```bash
python app.py
```

### Step 3: Open in Browser
Go to: **`http://localhost:5000`**

## Features

✨ **Real-Time Updates** - Clocks update every second
🌍 **7 Time Zones** - UTC, IST, EST, PST, GMT, JST, AEST
🎨 **Modern UI** - Responsive, dark-themed interface with animations
📱 **Mobile Friendly** - Works on phones, tablets, and desktops
⚡ **Fast & Efficient** - Optimized API and frontend
🔄 **Live Data** - Fetches time from server-side for accuracy

## Time Zones Displayed

| Zone | Location |
|------|----------|
| 🌐 UTC | Coordinated Universal Time |
| 🇮🇳 IST | India (Asia/Kolkata) |
| 🇺🇸 EST | US East Coast (US/Eastern) |
| 🇺🇸 PST | US West Coast (US/Pacific) |
| 🇬🇧 GMT | United Kingdom (Europe/London) |
| 🇯🇵 JST | Japan (Asia/Tokyo) |
| 🇦🇺 AEST | Australia (Australia/Sydney) |

## Project Structure

```
Airtel_suzuka/
├── app.py                 # Flask backend
├── room.py                # Tkinter desktop app
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Web UI
└── README.md             # This file
```

## Troubleshooting

### Port Already in Use
If port 5000 is in use, modify `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5000 to 5001
```

### Module Not Found
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Browser Won't Load
- Check if Flask is running (you should see messages in terminal)
- Try `http://127.0.0.1:5000` instead of `localhost:5000`
- Disable browser cache (Ctrl+Shift+Delete)

## Performance Optimizations

✅ Server-side timezone caching
✅ Single API call per update cycle
✅ Efficient JavaScript DOM updates
✅ Responsive grid layout
✅ Minimal re-renders

## License

Open source - Free to use and modify!

---

**Created by:** kapil175  
**Repository:** https://github.com/kapil175/Airtel_suzuka
