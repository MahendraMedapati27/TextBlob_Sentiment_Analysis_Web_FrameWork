# Sentiment Analysis Web Framework

This project is a web application for sentiment analysis using TextBlob and Flask. It allows users to input a single text for sentiment analysis or upload a CSV file containing multiple texts. The application processes the input and provides the sentiment (positive or negative) for each text. For CSV file inputs, it also generates a bar graph showing the count of positive and negative sentiments.

## Features

- **Analyze sentiment** of a single text input.
- **Upload a CSV file** for batch sentiment analysis.
- **Display results** in a user-friendly format.
- **Generate a bar graph** to visualize the sentiment distribution in the CSV file.

## Technology Stack

- **Python**
- **Flask**
- **TextBlob**
- **Pandas**
- **Matplotlib**
- **HTML**
- **CSS**

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/MahendraMedapati27/sentiment-analysis-web-framework.git
    cd sentiment-analysis-web-framework
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download NLTK data:**
    ```python
    import nltk
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Usage

1. **Run the Flask application:**
    ```sh
    python app.py
    ```

2. **Open your web browser and navigate to `http://127.0.0.1:5000/`.**

3. **Use the web interface to either:**
   - Enter a single text for sentiment analysis and click "Analyze".
   - Upload a CSV file (with a column named "text") for batch analysis and click "Analyze CSV".

## File Structure

sentiment-analysis-web-framework/
│
├── app.py
├── templates/
│ ├── index.html
│ ├── results.html
│ └── error.html
├── static/
│ ├── style.css
│ └── style2.css
├── requirements.txt
└── README.md


- **app.py:** The main Flask application file that contains the routes and logic for text processing and sentiment analysis.

- **templates/**: Contains the HTML templates for rendering the web pages.
  - `index.html`: The home page with forms for text input and CSV file upload.
  - `results.html`: The results page displaying sentiment analysis results and the bar graph.
  - `error.html`: The error page shows a error msg to upload the csv file or upload the text if the input is not given but the analyse button is pressed.

- **static/**: Contains the CSS files for styling the web pages.
  - `style.css`: Custom styles to make the web application more attractive.
  - `style2.css`: Additional styles for specific elements and responsiveness.

- **requirements.txt:** List of Python packages required to run the application.

- **README.md:** This file. Instructions and information about the project.

## Screenshots

### Home Page
![Home Page](path/to/homepage-screenshot.png)

### Results Page
![Results Page](path/to/results-page-screenshot.png)

## Contributing

1. **Fork the repository.**
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes.**
4. **Commit your changes** (`git commit -am 'Add some feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Create a new Pull Request.**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [TextBlob](https://textblob.readthedocs.io/en/dev/) - Python library for processing textual data.
- [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Micro web framework written in Python.
- [Matplotlib](https://matplotlib.org/) - Comprehensive library for creating static, animated, and interactive visualizations in Python.

## Contact

For any inquiries, please contact [mahendramedapati.r469@gmail.com](mailto:mahendramedapati.r469@gmail.com).








