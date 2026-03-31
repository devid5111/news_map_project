from flask import Flask, jsonify, request, render_template
from flask_cors import CORS 
from gnews import GNews

app = Flask(__name__)
CORS(app) 

# 1. FRONT-END PAGE LOAD
@app.route('/')
def home():
    
    # SEARCH FRONTED PAGE INTO TAMPLATES ... 
    
    return render_template('news_map_advanced.html')

# 2. Route: DICS NEWS COLLECT

@app.route('/api/news/<district>')
def get_news(district):
    print(f"Searching news for: {district}") 
    try:
        google_news = GNews(language='gu', country='IN', period='1d', max_results=15)
        news_items = google_news.get_news(f"{district} Gujarat")
        
        results = []
        for item in news_items:
            results.append({
                "title": item.get('title', 'No Title'),
                "source": item.get('publisher', {}).get('title', 'Unknown Source'),
                "time": item.get('published date', ''),
                "url": item.get('url', '#')
            })
        
        return jsonify({"news": results})
    except Exception as e:
        print(f"Error fetching district news: {e}")
        return jsonify({"news": []}), 500

# 3. Route: Search Bar 

def search_news():
    query = request.args.get('query', '')
    print(f"Searching for: {query}")
    try:
        google_news = GNews(language='gu', country='IN', period='1d', max_results=15)
        news_items = google_news.get_news(f"{query} Gujarat")
        
        results = []
        for item in news_items:
            results.append({
                "title": item.get('title', 'No Title'),
                "source": item.get('publisher', {}).get('title', 'Unknown Source'),
                "time": item.get('published date', ''),
                "url": item.get('url', '#')
            })
            
        return jsonify({"news": results})
    except Exception as e:
        print(f"Error searching news: {e}")
        return jsonify({"news": []}), 500

if __name__ == '__main__':
    # 
    app.run(port=5000, debug=True)