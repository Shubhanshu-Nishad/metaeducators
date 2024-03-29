# Meta Educator (Blogging and Educational Management Website)

This is a web application for a Blogging and Educational Management website. It is designed using HTML, CSS, JavaScript, Bootstrap, and the Django Python module for the backend.

## Features

1. User Registration and Login: Users can create an account and log in to the website. Their credentials will be securely stored in the backend.

2. Blogging Platform: Registered users can create, edit, and delete blog posts. Each blog post can have a title, content, and optional tags. Users can also comment on blog posts.

3. User Profile: Each user has a profile page where they can view and edit their personal information.

4. Educational Management: The website provides features to manage educational content such as courses, lessons, and quizzes. Administrators can add, edit, and delete courses and lessons. Users can enroll in courses and track their progress. Quizzes can be created with multiple-choice questions.

5. Responsive Design: The website is designed to be responsive and accessible across different devices and screen sizes.

## Technologies Used

The following technologies were used to develop this website:

- HTML: Used for the structure and layout of the web pages.
- CSS: Used for styling and customizing the appearance of the website.
- JavaScript: Used for client-side interactivity and dynamic content.
- Bootstrap: Used as a front-end framework for responsive design and pre-built components.
- Django: A high-level Python web framework used for the back-end development.

## Installation

To run the website locally, follow these steps:

1. Clone the repository to your local machine.
```
git clone https://github.com/Shubhanshu-Nishad/metaeducators.git
```

2. Navigate to the project directory.
```
cd metaeducators
```

3. Create a virtual environment (optional but recommended).
```
python -m venv myenv
```

4. Activate the virtual environment.
   - For Windows:
   ```
   myenv\Scripts\activate
   ```
   - For Linux/Mac:
   ```
   source myenv/bin/activate
   ```

5. Install the required Python dependencies.
```
pip install -r requirements.txt
```

6. Run the database migrations.
```
python manage.py migrate
```

7. Start the development server.
```
python manage.py runserver
```

8. Open your web browser and visit `http://localhost:8000` to access the website.

## Configuration

The website requires some configuration settings to function properly. These settings can be found in the `settings.py` file located in the `blogging-educational-management` directory. Make sure to update the following settings if needed:

- Database configuration: Set the appropriate database settings such as `DATABASES['default']['ENGINE']`, `DATABASES['default']['NAME']`, `DATABASES['default']['USER']`, and `DATABASES['default']['PASSWORD']`.

- Secret Key: Set the `SECRET_KEY` to a secure and random value.

- Email configuration: If you plan to use email-related features (e.g., account activation, password reset), configure the `EMAIL_BACKEND`, `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USE_TLS`, `EMAIL_HOST_USER`, and `EMAIL_HOST_PASSWORD` settings accordingly.

## Contributions

Contributions to the project are welcome. If you encounter any issues or would like to add new features, feel free to submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgements

- This project was developed using the Django web framework (https://www.djangoproject.com/).
- The Bootstrap framework (https://getbootstrap.com/) was used for the responsive design and pre-built components.
- Special thanks to the open-source community for their contributions and support.
