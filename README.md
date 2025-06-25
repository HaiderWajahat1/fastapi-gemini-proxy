# FastAPI Gemini Proxy

A lightweight FastAPI app that acts as a proxy to Google’s Gemini 1.5 Flash API. It forwards requests from your local server to the Gemini API using a secure API key stored in a `.env` file.

---

## 🔧 Local Setup

1. **Clone the repository**
```bash
git clone git@github.com:haiderwajahat1/fastapi-gemini-proxy.git
cd fastapi-gemini-proxy
```

2. **Create a virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. **Add your `.env` file**
In the root of the project, create a file called `.env`:
```env
GEMINI_API_KEY=your_api_key_here
```

4. **Run the FastAPI app**
```bash
uvicorn main:app --reload
```

- Open in browser: `http://localhost:8000/docs` to use Swagger UI.
- Postman URL: `http://localhost:8000/gemini` (POST)

---

## 🐳 Running with Docker

This app is Docker-ready and includes both a `Dockerfile` and a `docker-compose.yml`.

### 1. Build and run the container
```bash
docker-compose up --build
```

### 2. Access the app
Once running, access the FastAPI app at:
```
http://localhost:8000/docs   # Swagger UI
http://localhost:8000/gemini # POST endpoint for Gemini
```

### 3. Environment variable
Ensure you have a `.env` file with your Gemini API key. Docker will pick it up using the `env_file` setting in `docker-compose.yml`.

---

## 📬 Example POST Request

**URL:**
```
http://localhost:8000/gemini
```

**Body (JSON):**
```json
{
  "contents": [
    {
      "parts": [
        {
          "text": "Tell me a fun fact about space."
        }
      ]
    }
  ]
}
```

---

## ✅ Notes

- Use `.env` to keep your API key secure (never commit it).
- Can be tested with Postman, cURL, or Swagger UI.
- Fully containerized for easy sharing or deployment.
