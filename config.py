## config.py
PHONE_IP = "192.168.x.x"
PORT = 8022
USERNAME = "u0_a123"
PASSWORD = "your_password"

COMMANDS = {
    "toast": "termux-toast 'Hello Commander Dhruv'",
    "vibrate": "termux-vibrate -d 400",
    "battery": "termux-battery-status",
    "camera": "termux-camera-photo -c 0 ~/photo.jpg",
    "music": "termux-media-player play ~/Music/song.mp3",
    "location": "termux-location"
}
