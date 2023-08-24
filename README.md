# Article bucket

This Flask-based news article application provides users with a convenient way to access news articles from different sources and categories. Users can easily stay informed about current events and trending topics through a user-friendly web interface.

## Screenshot



## Features

- Fetches news articles from NewsAPI.
- Displays news articles in a user-friendly format.
- Allows users to search for specific topics.
- Allows users to read news from different categories.

## Installation

1. Clone this repository.

```bash
git clone https://github.com/yourusername/article-bucket.git
```

2. Go to the directory.

```bash
cd article-bucket
```

3. Create Virtual Environment.

```bash
python -m venv venv
```

4. Activate the Environment.

On Windows
```bash
venv\scripts\activate
```

On MacOS/Linux
```bash
source venv/bin/activate
```

5. Install the requirement package.

```bash
pip install -r requirements.txt
```

6. Run the Server.

```bash
flask run
```

## API Key

You need to set you NewsApi api_key in .env file and set this variable.

`API_KEY=your_news_api_key`