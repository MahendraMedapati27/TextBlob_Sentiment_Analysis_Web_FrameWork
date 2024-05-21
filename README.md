Sentiment Analysis Web Framework
This project is a web application for sentiment analysis using TextBlob and Flask. It allows users to input a single text for sentiment analysis or upload a CSV file containing multiple texts. The application processes the input and provides the sentiment (positive or negative) for each text. For CSV file inputs, it also generates a bar graph showing the count of positive and negative sentiments.

Features
Analyze sentiment of a single text input.
Upload a CSV file for batch sentiment analysis.
Display results in a user-friendly format.
Generate a bar graph to visualize the sentiment distribution in the CSV file.
Technology Stack
Python
Flask
TextBlob
Pandas
Matplotlib
HTML
CSS
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/MahendraMedapati27/sentiment-analysis-web-framework.git
cd sentiment-analysis-web-framework
Create and activate a virtual environment:

sh
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install the required packages:

sh
Copy code
pip install -r requirements.txt
Download NLTK data:

python
Copy code
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
Usage
Run the Flask application:

sh
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/.

Use the web interface to either:

Enter a single text for sentiment analysis and click "Analyze".
Upload a CSV file (with a column named "text") for batch analysis and click "Analyze CSV".
File Structure
arduino
Copy code
sentiment-analysis-web-framework/
│
├── app.py
├── templates/
│   ├── index.html
│   ├── results.html
│   └── error.html
├── static/
│   ├── style.css
│   └── style2.css
├── requirements.txt
└── README.md

app.py
The main Flask application file that contains the routes and logic for text processing and sentiment analysis.

templates/
Contains the HTML templates for rendering the web pages.

index.html: The home page with forms for text input and CSV file upload.
results.html: The results page displaying sentiment analysis results and the bar graph.
error.html: The error page shows a error msg to upload the csv file or upload the text if the input is not given but the analyse button is pressed.
static/
Contains the CSS file for styling the web pages.

style.css: Custom styles to make the web application more attractive.
requirements.txt
List of Python packages required to run the application.

README.md
This file. Instructions and information about the project.

Screenshots
Home Page

Results Page

Contributing
Fork the repository.
Create a new branch (git checkout -b feature-branch).
Make your changes.
Commit your changes (git commit -am 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
TextBlob - Python library for processing textual data.
Flask - Micro web framework written in Python.
Matplotlib - Comprehensive library for creating static, animated, and interactive visualizations in Python.
Contact
For any inquiries, please contact mahendramedapati.r469@gmail.com

Feel free to use this README template for your project and modify it according to your needs. Good luck with your project!







