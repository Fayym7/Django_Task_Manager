# Django Task Manager

A simple task management web application built using **Django** and **Google OAuth** for user authentication. The application allows users to manage their tasks, including creating, viewing, updating, and deleting tasks. Admin users can manage Google OAuth keys and invite users to the system via email.

## Features

- **Google Login**: Users can log in using their Google account.
- **Task Management**: Users can create, view, update, and delete tasks.
- **Admin Panel**: Admin users can manage Google OAuth keys, invite new users, and handle authentication configurations.
- **User Invitation**: Admins can send invitations to new users to register via the admin panel.

## Installation

Follow the steps below to get your development environment set up.

### Prerequisites

- Python 3.8 or higher
- Pip
- Virtual Environment (optional but recommended)

### 1. Clone the repository

Clone the repository to your local machine:
```bash
git clone https://github.com/Fayym7/Django_Task_Manager.git
cd Django-Task-Manager
```

### 2. Create and activate a virtual environment (optional but recommended)
Create a virtual environment:

```bash
python -m venv venv
```
Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
source venv/bin/activate
```
### 3. Install dependencies
Install the required Python packages:

```bash
pip install -r requirements.txt
```
### 4. Set up environment variables
Create a .env file in the project root and add the following sensitive keys (you can get the Google Client ID and Client Secret from the Google Developer Console):

```bash
DJANGO_SECRET_KEY=your-django-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
EMAIL_HOST_USER=your-email@example.com
EMAIL_HOST_PASSWORD=your-email-app-password
```
Make sure the .env file is included in .gitignore to keep your secrets safe.

### 5. Run migrations
Apply the database migrations to set up the database schema:

```bash
python manage.py migrate
```
### 6. Create a superuser (for admin access)
Create an admin user to access the Django Admin Panel:

```bash
python manage.py createsuperuser
```

### 7. Start the development server
Run the development server:

```bash
python manage.py runserver
```
You can now access the application by navigating to http://127.0.0.1:8000/ in your web browser.

## Features in Detail

### 1. Task Management:
Users can create, view, edit, and delete tasks.
Each task consists of a title and description, and users can mark tasks as completed.
Tasks are displayed on the homepage, with pagination available to navigate through tasks.

### 2. User Authentication (Google OAuth):
Users can log in using their Google account via django-allauth.
Upon successful login, users are redirected to the tasks page.
If a user hasn’t signed up yet, they will be prompted to complete the registration process.

### 3. Admin Panel:
Admin users can access the Django Admin Panel at /admin/.
Google OAuth keys can be managed by the admin.
User invitations can be sent via email by the admin, allowing new users to register.

### 4. User Invitations:
Admin users can send invitations to new users using the Admin Panel.
Invitations are sent to users with a unique registration link, allowing them to complete the registration process.

#### How Invitations Work:

The admin user can go to the User Invitation model in the admin panel.
There is an action called "Send invitation email" that sends an email to the invited user with a registration link.
The admin can view whether the invitation has been used or not.

## Admin Panel Features

### Managing Google OAuth Keys:
Admin users can manage the OAuth keys that enable Google login. These keys are stored in the database under the GoogleOAuthKey model.

### Inviting New Users:
Admin users can invite new users to register for the application. The system sends an invitation email with a registration link.

1. Navigate to the User Invitation model in the Django admin panel (/admin/).
2. Select one or more invitations and choose "Send invitation email" from the actions dropdown.
3. The system will send a unique registration link to the selected user's email address.

### View and Manage User Invitations:
The UserInvitation model includes fields for the email, token, is_used (whether the invitation has been used), and created_at.
Admin users can track the status of invitations directly in the admin interface.

## Configuration Options
You can modify the following settings in your settings.py file:

### Google OAuth Configuration:
GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET: Set these values to the OAuth credentials provided by Google.

### Email Settings:
EMAIL_HOST_USER and EMAIL_HOST_PASSWORD: Set these values to enable the email sending functionality for user invitations.

## Notes
Security: The application uses environment variables to securely store sensitive data like the SECRET_KEY, Google OAuth credentials, and email configuration.
Deployment: This application is intended to be deployed in a production environment with proper security measures, including HTTPS and secure handling of credentials.
