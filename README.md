# Article bucket

This Flask-based news article application provides users with a convenient way to access news articles from different sources and categories. Users can easily stay informed about current events and trending topics through a user-friendly web interface.

## Screenshots

### Home Page showing latest news.

![Home Page](https://github.com/anuraagnagar/article-bucket/blob/main/content/screenshots/home_page.png)

### Category Page showing according to listed category.

![Category Page](https://github.com/anuraagnagar/article-bucket/blob/main/content/screenshots/category_page.png)

### Search news according to your need.

![Search Page](https://github.com/anuraagnagar/article-bucket/blob/main/content/screenshots/search_page.png)

## Library & Modules

- ![FLask](https://flask.palletsprojects.com/)
- ![FLask-Caching](https://flask-caching.readthedocs.io/en/latest)
- ![Newsapi-Python](https://newsapi-python.readthedocs.io/en/latest)
- ![Jinja2](https://jinja.palletsprojects.com/)

## Features

- Fetches news articles from NewsAPI.
- Displays news articles in a user-friendly format.
- Allows users to search for specific topics.
- Allows users to read news from different categories.

## Installation & Set Up Locally.

### Prerequisites

- Python 3.x
- Virtual environment tool (e.g., venv or virtualenv)
- Git (optional, but recommended for cloning the repository)

### 1. Clone this repository.

```bash
git clone https://github.com/anuraagnagar/article-bucket.git
```

### 2. Go to the directory.

```bash
cd article-bucket
```

### 3. Create Virtual Environment.

```bash
python -m venv venv
```

### 4. Activate the Environment.

On Windows

```bash
venv\scripts\activate
```

On MacOS/Linux

```bash
source venv/bin/activate
```

## API Key

You need to convert `.env.example` to `.env` file in your base directory and set your newsapi `API_KEY` environment variable value.

### 5. Install the requirement package.

```bash
pip install -r requirements.txt
```

### 6. Run the Server.

```bash
flask run
```

To access this application open `http://localhost:5000` in your web browser.

## Contributing

Contributions are welcome! If you find a bug or want to add a new feature, please open an issue or submit a pull request.
For more information checkout ![CONTRIBUTING.md](https://github.com/anuraagnagar/article-bucket/blob/main/CONTRIBUTING.md)

## Licence

By contributing to this project, you agree that your contributions will be licensed under the ![MIT License](https://github.com/anuraagnagar/article-bucket/blob/main/LICENSE).
