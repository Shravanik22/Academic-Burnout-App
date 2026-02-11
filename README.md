# Academic-Burnout-App
🎓 Academic Burnout & Deadline Collision Detector - A smart web app helping students manage workload, detect deadline conflicts, and prevent burnout through data-driven insights and collaborative task management.

# 📚 Academic Burnout & Deadline Collision Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red.svg)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🎯 Overview

A comprehensive web-based application designed to help students manage academic workload, detect deadline collisions, analyze burnout risk, and facilitate group collaboration for better time management and reduced stress levels.

## 🚀 Features

### Core Functionality
- ✅ **User Authentication** - Secure registration, login, and password reset
- 📋 **Individual Task Management** - Add, edit, delete, and track personal assignments
- 👥 **Group Collaboration** - Role-based task management (Head & Member)
- ⚠️ **Deadline Collision Detection** - Automatic detection of same-day deadlines
- 🔥 **Burnout Risk Analysis** - AI-powered workload assessment (Low/Medium/High)
- 📅 **Calendar Views** - Monthly, weekly, and list views
- 📊 **Interactive Analytics** - Charts and graphs using Plotly
- 📥 **Export Reports** - Excel (.xlsx) and PDF export functionality
- 🔔 **Smart Reminders** - 3-day advance deadline notifications

### Advanced Features
- 🎯 **Automatic Priority Calculation** - Based on estimated hours
- 👑 **Role-Based Access Control** - Different permissions for group heads and members
- 🔐 **Invite Code System** - Unique 8-character codes for joining groups
- 📈 **Progress Tracking** - Completion percentages and statistics
- 🎨 **Modern UI** - Professional gradient design with responsive layout
- ✔️ **Task Completion Tracking** - Separate views for active and completed tasks

## 🛠️ Tech Stack

**Frontend:**
- Streamlit - Web framework
- Plotly - Interactive charts and visualizations
- Custom CSS - Modern UI design

**Backend:**
- Python 3.11
- MySQL - Database management
- bcrypt - Password encryption

**Libraries:**
- `streamlit` - User interface
- `mysql-connector-python` - Database connectivity
- `bcrypt` - Secure password hashing
- `plotly` - Data visualization
- `fpdf` - PDF generation
- `openpyxl` - Excel export
- `pillow` - Image handling

## 📁 Project Structure
```
academic_burnout_app/
├── app.py                  # Main application with all pages
├── auth.py                 # Authentication & password management
├── db.py                   # Database connection & queries
├── tasks.py                # Individual task management
├── groups.py               # Group & collaboration features
├── burnout.py              # Burnout risk calculation
├── calendar_sync.py        # Calendar integration
├── utils.py                # UI helpers & export functions
├── schema.sql              # Database schema
└── requirements.txt        # Python dependencies
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.11 or higher
- MySQL Server 8.0 or higher

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/academic-burnout-detector.git
cd academic-burnout-detector
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Setup Database
```bash
# Login to MySQL
mysql -u root -p

# Create database and tables
mysql -u root -p < schema.sql
```

### Step 4: Configure Database Connection
Update `db.py` with your MySQL credentials:
```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'academic_burnout_db'
}
```

### Step 5: Run the Application
```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 📖 Usage Guide

### For Individual Students:
1. **Register** - Create account with secure password
2. **Add Tasks** - Enter title, deadline, and estimated hours
3. **Track Progress** - View tasks in calendar and list views
4. **Monitor Burnout** - Check risk level on dashboard
5. **Mark Complete** - Update task status as you finish
6. **Export Data** - Download reports in Excel or PDF

### For Group Projects:
1. **Create Group** - Get unique invite code
2. **Invite Members** - Share code with team
3. **Assign Tasks** - Heads assign work to members
4. **Track Status** - Update progress (Pending → In Progress → Completed)
5. **View Analytics** - Monitor group completion rate

## 🎯 Key Algorithms

### Priority Calculation
```python
if estimated_hours <= 2:
    priority = "Low"
elif estimated_hours <= 4:
    priority = "Medium"
else:
    priority = "High"
```

### Burnout Risk Assessment
```python
risk_score = 0
if total_tasks >= 10: risk_score += 2
if tasks_due_week >= 5: risk_score += 2
if total_hours_week >= 20: risk_score += 3

if risk_score >= 5: risk_level = "High"
elif risk_score >= 3: risk_level = "Medium"
else: risk_level = "Low"
```

## 📊 Screenshots

Welcome Page-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 225406" src="https://github.com/user-attachments/assets/c97ebf8f-011b-45af-8f38-6979fa5270ad" />

Registration Page-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 225636" src="https://github.com/user-attachments/assets/1f56bbc3-55cc-45b7-9812-a06978c2549d" />

Login Page-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 225728" src="https://github.com/user-attachments/assets/88f217e8-cade-4e08-bf33-4de035ba217b" />

Dashboard -
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231252" src="https://github.com/user-attachments/assets/ae9896ae-8fe8-43eb-9ffb-c9f2f2719c78" />
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231318" src="https://github.com/user-attachments/assets/9be0d7b6-f190-417e-b94f-cbdda8f8b06d" />

Individual Task-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231405" src="https://github.com/user-attachments/assets/2bbf55b5-4b54-4973-bbf4-68faf8cffd3f" />

Group Tasks-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231538" src="https://github.com/user-attachments/assets/027132fe-45b1-4721-8d39-bed4897fb03b" />

Calendar -
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231754" src="https://github.com/user-attachments/assets/ce162025-cc13-4e7d-b463-9ef4f06e999f" />

Reports & Analysis-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231840" src="https://github.com/user-attachments/assets/c9dae21a-c204-44e3-ba40-698630767b00" />
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231857" src="https://github.com/user-attachments/assets/5a2a28fa-6395-4bc6-bdf9-ce64e3ada75d" />

Burnout Analysis-
<img width="1920" height="1080" alt="Screenshot 2026-02-06 231924" src="https://github.com/user-attachments/assets/21e2431c-dc0a-40e1-b79b-4ca8ec9a5033" />

- Dashboard with burnout analysis
- Task management interface
- Group collaboration page
- Calendar view
- Analytics and reports

## 🎓 Learning Outcomes

This project helped us learn:
- Full-stack web application development
- Database design and SQL queries
- User authentication and security
- Data visualization with Plotly
- Collaborative software development
- UI/UX design principles
- Agile project management

## 🔮 Future Enhancements

- [ ] Mobile application (Android/iOS)
- [ ] Email notifications
- [ ] Google Calendar integration
- [ ] Task categories/subjects
- [ ] File upload for assignments
- [ ] Group chat functionality
- [ ] Dark mode theme
- [ ] Multi-language support
- [ ] AI-powered workload balancing
- [ ] Recurring tasks

## 👥 Team Members

- **Mahek Kala** - [LinkedIn](https://www.linkedin.com/in/mahek-kala-a14b9332b)
- **Shravani Kumbhar** - [LinkedIn](https://www.linkedin.com/in/shravani-kumbhar-373b9532b)
- **Monishka Mahulkar** - [LinkedIn](https://www.linkedin.com/in/monishka-mahulkar-484962377)

## 🏫 Institution

**Shah And Anchor Kutchhi Engineering College**
- Class: SY IT (2)
- Subject: Python Programming
- Academic Year: 2025-2026

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Streamlit community for excellent documentation
- Plotly for interactive visualization library
- Our college faculty for guidance and support
- All students who tested and provided feedback

## 📧 Contact

For questions or feedback, please reach out:
- Email: shravanikumbhar318@gmail.com
- LinkedIn: [(https://www.linkedin.com/in/shravani-kumbhar-373b9532b)]

## ⭐ Show your support

Give a ⭐️ if this project helped you!

---

**Made with ❤️ by Team Academic Burnout Detector**

