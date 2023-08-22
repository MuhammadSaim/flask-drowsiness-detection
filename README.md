# Flask Drowsiness Detection

## Requirements
- Python
- Flask
- Flask SQLAlchemy
- Flask Migrate


### Technologies

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![PyPi](https://img.shields.io/badge/pypi-3775A9?style=for-the-badge&logo=pypi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![PyCharm](https://img.shields.io/badge/PyCharm-000000.svg?&style=for-the-badge&logo=PyCharm&logoColor=white)
![jQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![AJAX](https://img.shields.io/badge/ajax-000000?style=for-the-badge&logo=ajax&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![SASS](https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white)
![OpenCV](https://img.shields.io/badge/opencv-F7DF1E?style=for-the-badge&logo=opencv&logoColor=red)


### Configuration

1. Clone the repo
```shell
git clone git@github.com:MuhammadSaim/flask-drowsiness-detection.git
```
2. Step into folder
```shell
cd blog
```
3. Create virtual environment
```shell
virtualenv venv 
```
4. Activate the venv
```shell
source venv/bin/activate
```
5. Install the dependencies
```shell
pip install -r requirements.txt
```

6. Copy the <kbd>.env.example</kbd> to <kbd>.env</kbd> and setup your DB on <kbd>.env</kbd>

7. Setup the DB
```.dotenv
SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://DB_USERNAME:DB_PASSWORD@127.0.0.1:3306/DB_DATABASE"
```

8. Run the migrations.
```shell
flask db upgrade
```

9. Install frontend dependencies
```shell
# if you have yarn
yarn install

# if you have npm
npm install
```

10. Build the assets
```shell
# if you have yarn
yarn watch
# or
yarn dev

# if you have npm
npm run watch
# or
npm run dev
```

11. Run the flask app
```shell
python run.py
```