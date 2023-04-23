# VideoM8
The VideoM8 is my variation of VOD platform,
dedicated for movies. Allows users to find a
favorite movie and watch it.
## Tech Stack

* **Frontend:** Bootstrap 5.3 
* **Backend:** python 3.11, Django 4.1.5
* **Databases:** PostgreSQL

## Getting Started 
### 1. Clone the project repository:

 https://github.com/Uncle-Moris/VideoM8.git 

### 2. Create a virtual environment for the project: 
#### On Windows
```bash
python -m venv myenv
```


#### On macOS or linux 
```bash
python3 -m venv myenv
```


### 3. Install project dependencies:
```bash
pip install -r requirements.txt
```
### 4. Create database migrations and apply them:
```bash
python manage.py makemigrations 

python manage.py migrate
 ```

### 5. Start the development server:
```bash
python manage.py runserver
```

### 6. Open app
Open a web browser and navigate to http://127.0.0.1:8000/ to access the VideoM8 app.