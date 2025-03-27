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

1️⃣ Create a Post

URL: POST /api/posts/

Headers:

{
    "Authorization": "Token your_generated_token"
}

Request Body:

{
    "title": "My First Post",
    "content": "This is my first post content."
}

Response:

{
    "id": 1,
    "author": "john_doe",
    "title": "My First Post",
    "content": "This is my first post content.",
    "created_at": "2025-03-24T12:00:00Z",
    "updated_at": "2025-03-24T12:00:00Z"
}

2️⃣ Get All Posts (Paginated)

URL: GET /api/posts/?page=1

Headers:

{
    "Authorization": "Token your_generated_token"
}

Response:

{
    "count": 100,
    "next": "http://127.0.0.1:8000/api/posts/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "author": "john_doe",
            "title": "My First Post",
            "content": "This is my first post content.",
            "created_at": "2025-03-24T12:00:00Z",
            "updated_at": "2025-03-24T12:00:00Z"
        }
    ]
}

3️⃣ Update a Post

URL: PUT /api/posts/1/

Headers:

{
    "Authorization": "Token your_generated_token"
}

Request Body:

{
    "title": "Updated Post Title",
    "content": "Updated post content."
}

4️⃣ Delete a Post

URL: DELETE /api/posts/1/

Headers:

{
    "Authorization": "Token your_generated_token"
}

📝 Comment API Endpoints

1️⃣ Create a Comment

URL: POST /api/comments/

Headers:

{
    "Authorization": "Token your_generated_token"
}

Request Body:

{
    "post": 1,
    "content": "This is a comment."
}

2️⃣ Get Comments for a Post

URL: GET /api/comments/

3️⃣ Update a Comment

URL: PUT /api/comments/1/

4️⃣ Delete a Comment

URL: DELETE /api/comments/1/

For any issues, please open a GitHub issue or reach out to the maintainer. 🚀

Unfollow a User
POST /api/unfollow/{user_id}/
Allows the authenticated user to unfollow another user.

Request:

json
Copy
Edit
{
    "action": "unfollow"
}
Response:

json
Copy
Edit
{
    "message": "You have unfollowed user_id."
}
Errors:

400 Bad Request if the user was not being followed.

404 Not Found if the target user does not exist.

3. Get User's Followers
GET /api/user/{user_id}/followers/
Retrieves a list of followers for a user.

Response:

json
Copy
Edit
{
    "followers": [
        {
            "id": 2,
            "username": "john_doe",
            "profile_picture": "https://example.com/profile_pics/john.jpg"
        },
        {
            "id": 3,
            "username": "jane_smith",
            "profile_picture": "https://example.com/profile_pics/jane.jpg"
        }
    ]
}
3.4 Get User's Following List
GET /api/user/{user_id}/following/
Retrieves a list of users that the specified user is following.

Response:

json
Copy
Edit
{
    "following": [
        {
            "id": 5,
            "username": "mike_jones",
            "profile_picture": "https://example.com/profile_pics/mike.jpg"
        }
    ]
}
3. Get User Feed
GET /api/user/feed/
Fetches a personalized feed from followed users.

Response:

json
Copy
Edit
{
    "feed": [
        {
            "post_id": 10,
            "author": "jane_smith",
            "content": "New blog post is up!",
            "created_at": "2025-03-24T12:00:00Z"
        },
        {
            "post_id": 15,
            "author": "john_doe",
            "content": "Great weather today!",
            "created_at": "2025-03-24T14:30:00Z"
        }
    ]
}
4. Model Changes
4.1 CustomUser Model Updates
Added followers and following ManyToMany relationships.

Introduced the Follow model for a more structured following system.

4.2 Follow Model
python
Copy
Edit
class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name="following_relations", on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name="follower_relations", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"
5. Notes
Ensure migrations are applied:

sh
Copy
Edit
python manage.py makemigrations
python manage.py migrate
The feed system can be expanded to include more content types like images and videos.

Rate limiting can be implemented to prevent spam.



