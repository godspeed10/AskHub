Project Setup Instructions (AskHub)
Clone the Repository

  git clone <your-repo-url>
  cd <your-project-folder>


Create a Virtual Environment

  python -m venv venv
  Activate the Virtual Environment

Windows:
  venv\Scripts\activate

bash
  source venv/bin/activate
  Install Dependencies



pip install -r requirements.txt


Apply Migrations


  python manage.py makemigrations
  python manage.py migrate

  
Create a Superuser (Admin)
  python manage.py createsuperuser

  
Follow the prompts to set username, email, and password.

Run the Development Server
  python manage.py runserver



Access the App
  Main App: http://127.0.0.1:8000/app/
  
  Admin Panel: http://127.0.0.1:8000/admin/
