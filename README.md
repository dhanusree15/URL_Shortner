# URL Shortener Web Application

This repository contains code for a simple URL shortener web application built using Flask and JavaScript. The application allows users to enter a long URL, and it generates a shortened version using the TinyURL API.

## Project Structure

- `app.py`: Flask application file containing the server-side code.
- `templates/index.html`: HTML template for the web interface.
- `static/style.css`: CSS file for styling the HTML template.

## How It Works

1. Run the Flask application using `python app.py`.
2. Access the web interface at `http://127.0.0.1:5000/` in your browser.
3. Enter a long URL in the input field.
4. Click the "Shorten URL" button.
5. The application sends a request to the server (`/shorten` endpoint) using JavaScript's `fetch` API.
6. The server uses the `pyshorteners` library to generate a TinyURL for the provided long URL.
7. The server responds with the shortened URL, and it is displayed on the web interface.

## Requirements

- Flask
- pyshorteners
- pyperclip (not explicitly used but imported)

