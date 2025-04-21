

```markdown
🧳 PackPal – Group Logistics Organizer
PackPal is a collaborative web application designed to streamline event and travel packing by enabling teams to assign items, monitor packing progress, and work together in real-time.

Built as a hackathon project, PackPal supports role-based access, conflict alerts, and real-time item status updates to ensure smooth group organization.

---

🔑 Key Features

- ✅ Role-Based Access: Owner, Admin, Member, Viewer
- 📋 Collaborative Checklists: Organize items by category
- 🚦 Item Status Tracking: To Pack, Packed, Delivered
- 🔄 Real-Time Updates: Track who packed what, instantly
- ⚠️ Conflict Alerts: Prevent duplicate items and assignments
- 📊 Progress Dashboard: View status of team packing at a glance

---

💻 Tech Stack

| Layer     | Tech                                      |
|-----------|-------------------------------------------|
| Frontend  | HTML, CSS, Bootstrap                      |
| Backend   | Python, Flask, Flask-SocketIO             |
| Database  | MySQL                                     |
| Server    | Werkzeug (for dev), ready for Gunicorn    |

---

📁 Project Structure

```
PackPal/
│
├── app.py                  # Main Flask app
├── db.py                   # MySQL DB connector
├── schema.sql              # SQL schema for PackPal DB
├── requirements.txt        # Python packages
│
├── templates/              # HTML templates
│   ├── signup.html
│   ├── login.html
│   ├── dashboard.html
│   └── ...
│
└── static/                 # (Optional) CSS/JS/images
```

---

🛠️ Setup Instructions

1. Clone the Repository

```bash
git clone https://github.com/your-username/packpal.git
cd packpal
```

---

🧪 Sample Roles

| Role   | Permissions                                |
|--------|--------------------------------------------|
| Owner  | Create events, assign roles, manage all    |
| Admin  | Manage checklists and users in event       |
| Member | Mark items, participate in checklist       |
| Viewer | Read-only access                           |

---

🚀 Future Enhancements

- 🔔 Push Notifications
- 📱 Mobile App (Flutter)
- 📆 Calendar/Event Integration
- 📦 Auto-suggestions for packing lists

---

👨‍💻 Author

Made with 💙 at Tic-Tech_Toe Hackathon 2025

---

📄 License

This project is licensed under the MIT License.
```
