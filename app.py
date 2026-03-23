from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/suggest')
def suggest():
    import requests

    url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070?api-key=guest&format=json&limit=10"

    crops = []

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            for item in data.get('records', []):
                try:
                    crop = item.get('commodity', 'N/A')
                    price = int(item.get('modal_price', 0))
                    crops.append({"crop": crop, "price": price})
                except:
                    continue

    except:
        pass

    
    if not crops:
        crops = [
            {"crop": "Tomato", "price": 1200},
            {"crop": "Onion", "price": 1500},
            {"crop": "Rice", "price": 2000}
        ]

    best = max(crops, key=lambda x: x['price'])

    return f"Best crop to sell today: {best['crop']} (₹{best['price']})"
if __name__ == '__main__':
    app.run(debug=True)