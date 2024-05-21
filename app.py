from flask import Flask, request, render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Function for text preprocessing
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    text = ' '.join(words)
    return text

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        if 'text' in request.form:  # Analyze single text input
            text = request.form['text']
            processed_text = preprocess_text(text)
            analysis = TextBlob(processed_text)
            sentiment = 'Positive' if analysis.sentiment.polarity > 0 else 'Negative'
            return render_template('index.html', text=text, processed_text=processed_text, sentiment=sentiment)
        
        elif 'file' in request.files:  # Analyze uploaded CSV file
            file = request.files['file']
            if file.filename.endswith('.csv'):
                df = pd.read_csv(file)
                df['processed_text'] = df['text'].apply(preprocess_text)
                df['sentiment'] = df['processed_text'].apply(lambda x: 'Positive' if TextBlob(x).sentiment.polarity > 0 else 'Negative')
                
                # Create bar graph
                sentiment_counts = df['sentiment'].value_counts()
                plt.figure(figsize=(10, 6))
                colors = ['#66b3ff', '#ff9999']
                sentiment_counts.plot(kind='bar', color=colors, edgecolor='black')
                plt.xlabel('Sentiment')
                plt.ylabel('Count')
                plt.title('Sentiment Analysis')
                plt.xticks(rotation=0)
                plt.grid(axis='y', linestyle='--', linewidth=0.7)

                # Convert plot to base64 string
                buffer = io.BytesIO()
                plt.savefig(buffer, format='png', bbox_inches='tight')
                buffer.seek(0)
                image_png = buffer.getvalue()
                buffer.close()
                graph = base64.b64encode(image_png).decode()

                # Display results and bar graph
                return render_template('results.html', data=df.to_html(index=False), graph=graph)
            else:
                return render_template('error.html', message='Please upload a CSV file.')
        else:
            return render_template('error.html', message='No input received.')

if __name__ == '__main__':
    app.run(debug=True)





