# Social Media API - README

##  Overview
This is a Django-based **Social Media API** that provides user authentication, profile management, and token-based authentication using Django REST Framework (DRF).

# Features
- User Registration (returns authentication token upon success)
- User Login (returns authentication token upon success)
- User Profile Management (retrieve & update profile)
- Token-based Authentication

---

## Setup Instructions

### **1️⃣ Clone the Repository**
```bash
 git clone https://github.com/yourusername/Alx_DjangoLearnLab.git
 cd Alx_DjangoLearnLab/social_media_api
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure the Database**
Apply migrations to create the necessary database tables:
```bash
python manage.py migrate
```

### **5️⃣ Create a Superuser (Optional for Admin Panel)**
```bash
python manage.py createsuperuser
```

### **6️⃣ Run the Server**
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/`

---

##  Authentication Endpoints

### **1️⃣ Register a User**
- **URL:** `POST /api/auth/register/`
- **Request Body:**
```json
{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "securepassword"
}
```
- **Response:**
```json
{
    "token": "generated_token_here",
    "user": {
        "id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    }
}
```

### **2️⃣ Login a User**
- **URL:** `POST /api/auth/login/`
- **Request Body:**
```json
{
    "username": "john_doe",
    "password": "securepassword"
}
```
- **Response:**
```json
{
    "token": "generated_token_here",
    "user_id": 1,
    "username": "john_doe"
}
```

### **3️⃣ Get User Profile** (Authenticated Users Only)
- **URL:** `GET /api/auth/profile/`
- **Headers:**
```json
{
    "Authorization": "Token your_generated_token"
}
```
- **Response:**
```json
{
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "bio": "",
    "profile_picture": null,
    "followers": []
}
```

---

##  User Model Overview
The `CustomUser` model extends Django's `AbstractUser` and includes:
- `bio` (TextField) - Optional user bio.
- `profile_picture` (ImageField) - User profile picture.
- `followers` (ManyToManyField) - A self-referencing ManyToMany field for user relationships.

```python
class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
```

---

## 🛠 Additional Features Coming Soon
- Password Reset
- Friend Requests
- Post & Comment System

For any issues, please open a GitHub issue or reach out to the maintainer. 🚀

