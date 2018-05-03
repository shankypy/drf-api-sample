# drf-api-sample

# Scope of the project
- Admin can create/delete/edit a group.
- Admin can create/edit/delete a user;
- Admin can assign task to non-admin/non-staff user.
- non-admin/non-staff user can check his task only.
- non-admin/non-staff user can update his task progress(field) in terms of the number of times the task has beed done.
- Admin can assign task to a group.
- Multiple admins can assign on task to different user.
- Admin can review non-staff/non-admin user's task progress.

# Dependencies
Django==1.11.10
djangorestframework==3.8.2

# Installation
1. Clone this repository: git clone https://github.com/shankypy/drf-api-sample.git
2. Create virtual environment: virtualenv -p python3.5 venv
3. Activate your environment: source venv/bin/activate
4. cd into usermanagement: cd usermanagement
5. Install dependecies: pip install -r requirements.txt
6. Starts server: python manage.py runserver


Note: Make sure virtualenv and python3.5 are installed. All of these dependencies are mentioned in the 'requirements.txt' file
