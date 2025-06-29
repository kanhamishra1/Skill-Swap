# 🔄 SkillSwap

**SkillSwap** is a full-stack web application that enables peer-to-peer skill exchange. Users can register, list the skills they want to teach or learn, and connect with others for knowledge sharing.

---

## 🚀 Features

- 🔐 JWT-based authentication
- 👤 User registration & profile management
- 🧠 List skills you can teach or want to learn
- 🔍 Match with users based on skill interests
- 📬 (Upcoming) Chat or connect system for communication

---

## 🛠️ Tech Stack

| Layer      | Technology              |
|------------|--------------------------|
| Backend    | Django, Django REST Framework |
| Frontend   | React  |
| Auth       | JWT (JSON Web Token)     |
| Database   | SQLite (can upgrade to PostgreSQL later) |
| Dev Tools  |  GitHub, Postman,PyCharm |

---

## 🧩 Folder Structure (Backend)

skillswap-backend/
│
├── apps/
│ ├── accounts/
│ └── skillswap_backend/
│
├── manage.py
├── requirements.txt
├── db.sqlite3
├── .gitignore

📦 2. Create and Activate Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
📥 3. Install Dependencies

pip install -r requirements.txt
⚙️ 4. Run Migrations

python manage.py makemigrations
python manage.py migrate

▶️ 5. Start Development Server

python manage.py runserver

🧪 API Testing (with Postman)
Import POST /register/ to register a user

Use POST /login/ to get JWT token

Pass token in Authorization header: Bearer <your-token>

Access protected endpoints like /profile/, /update-profile/, etc.

📌 Status
🚧 Project is under active development

🙋‍♂️ Author
Balgopal Mishra
Email: kanhamishra1a@gmail.com
LinkedIn: www.linkedin.com/in/BalGopalMishra07
GitHub: @kanhamishra1


