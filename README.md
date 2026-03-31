# 🌍 Live News Explorer Map

An interactive full-stack web application that visualizes real-time local news on a geographical map.
Users can click on any district in Gujarat and instantly view the latest headlines from that region.

---

## 🚀 Features

* 🗺️ Interactive map using Leaflet.js
* 📍 District-based news fetching
* ⚡ Real-time news updates via API
* 🔎 Search functionality for custom queries
* 🌙 Dark Mode support
* 💀 Skeleton loading UI for better UX
* 📱 Fully responsive design

---

## 🛠️ Tech Stack

### Frontend

* HTML5
* CSS3 (with variables for theming)
* JavaScript (Fetch API, Promises)
* Leaflet.js (Map integration)

### Backend

* Python
* Flask
* GNews API

---

## 📂 Project Structure

```
Live-News-Explorer/
│
├── app2.py                     # Flask backend (API + routing)
│
├── templates/
│   └── news_map_advanced.html # Main frontend UI (map + dashboard)
│
├── static/ (optional if added later)
│   ├── css/
│   ├── js/
│   └── assets/
│
├── requirements.txt           # Python dependencies
│
└── README.md                  # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/live-news-explorer.git
cd live-news-explorer
```

### 2. Create virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install flask flask-cors gnews
```

### 4. Run the server

```bash
python app2.py
```

### 5. Open in browser

```
http://127.0.0.1:5000/
```

---

## 🔌 API Endpoints

### Get News by District

```
GET /api/news/<district>
```

**Example:**

```
/api/news/Ahmedabad
```

---

### Search News

```
GET /api/search?query=<keyword>
```

**Example:**

```
/api/search?query=election
```

---

## 💡 How It Works

1. User clicks on a district on the map
2. Frontend sends request to Flask API
3. Backend fetches news using GNews
4. Data is formatted and sent as JSON
5. UI dynamically renders news cards

---

## ⚠️ Known Issues / Improvements

* Search route must be properly registered (`/api/search`)
* Map tile layers may stack on theme toggle (needs cleanup)
* Limited results when using Gujarati language filter
* No caching → API calls every time

---

## 🔮 Future Enhancements

* 🌐 Multi-state / global expansion
* 📊 News analytics & trends
* 🧠 AI-based summarization
* 🔔 Notifications for breaking news
* 🗂️ Category filters (Sports, Politics, Tech)

---

## 👨‍💻 Author

**Your Name**
Student Developer | Full Stack Enthusiast

---

## 📜 License

This project is open-source and available under the MIT License.

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share your feedback!
