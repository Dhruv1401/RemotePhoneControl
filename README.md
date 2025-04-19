# RemoteTermuxController 🚀

Control your Android phone wirelessly using Termux + SSH + Python + Flask. No root required.

---

## 📱 Termux Setup (On Your Android)

### Step 1: Install Termux
- Download from [F-Droid](https://f-droid.org/en/packages/com.termux/)

### Step 2: Configure Termux
```bash
pkg update && pkg upgrade
pkg install termux-api openssh python git -y
git clone https://github.com/Dhruv1401/RemoteTermuxController
cd RemoteTermuxController
termux-setup-storage
passwd  # Set SSH password
sshd    # Start SSH server
```

### Step 3: Find Your IP
```bash
ifconfig  # Look for wlan0 -> 192.168.x.x
```

Allow all permissions in **Settings > Apps > Termux > Permissions**.

---

## 💻 PC Setup

### Step 1: Clone Repo & Install Requirements
```bash
git clone https://github.com/yourusername/RemoteTermuxController
cd RemoteTermuxController
pip install -r requirements.txt
```

### Step 2: Edit config.py
Update your:
- PHONE_IP
- USERNAME (`u0_a123` or whatever your Termux shell shows)
- PASSWORD

---

## 🔧 Usage

### CLI
```bash
python controller.py
```

### Flask Web Panel
```bash
python app.py
```
Then open `http://localhost:5000` or `http://<your-pc-ip>:5000` from your browser.

---

## 🔐 Notes
- Keep phone & PC on same WiFi network
- Port is 8022 by default for Termux SSH
- You can customize commands in `config.py`

---

## 🧠 Ideas to Expand
- Auto location sender
- Motion detection via camera
- Remote file access
- Send text messages
- Full AI assistant integration 😉

---

Made with ❤️ by Dhruv1401 and ChatGPT.
