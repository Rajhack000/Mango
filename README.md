# Network Traffic Analyzer

🕵️ A real-time network traffic analyzer that intercepts and displays network requests from websites.

## Features

- Intercept fetch and XMLHttpRequest API calls
- View request and response details
- Filter requests by method or type
- Export results to JSON
- Clean, responsive UI with a hacker-style theme

## Demo

![Network Traffic Analyzer Demo](https://i.imgur.com/placeholder.gif)

## How to Use

### Online Version

Access the hosted version at (your-deployed-streamlit-url).

### Run Locally

1. Clone this repository
   ```
   git clone https://github.com/yourusername/network-traffic-analyzer.git
   cd network-traffic-analyzer
   ```

2. Install dependencies
   ```
   pip install -r requirements.txt
   ```

3. Run the Streamlit app
   ```
   streamlit run app.py
   ```

4. Open your browser to the URL displayed in the terminal (usually http://localhost:8501)

## How It Works

The analyzer works by overriding the native fetch and XMLHttpRequest APIs to intercept all network requests made within the iframe. It captures request details including:

- Request method and URL
- Headers
- Request body
- Response data and status

## Limitations

Due to browser security restrictions:
- Some requests may be blocked by CORS policies
- Requests from other origins or secure contexts may not be visible
- This tool is meant for educational and development purposes only

## License

MIT 