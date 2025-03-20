
# OpenAI FastAPI Starter 🚀

A clean, production-ready starter project built using **FastAPI** and **OpenAI GPT APIs**.  
This template is designed to help you quickly build AI-powered APIs with environment-based configuration, clean architecture, and easy scalability.

---

## ✅ Features
- 🔹 FastAPI-based asynchronous API
- 🔹 OpenAI GPT integration (ChatCompletion)
- 🔹 Clean project structure with service layers
- 🔹 Separate environment configs for dev, staging, and production
- 🔹 Auto-validation and OpenAPI docs (thanks to Pydantic)
- 🔹 Logging setup for clean debugging and production monitoring
- 🔹 Ready-to-use `run_local.sh` script for quick start
- 🔹 Example `/generate` endpoint for AI text generation

---

## ✅ Project Structure
```
app/
 ├── main.py               # FastAPI entry point
 ├── api/
 │   └── v1/endpoints.py   # Route definitions
 ├── core/
 │   ├── config.py         # Environment configurations
 │   └── openai_client.py  # OpenAI API wrapper
 ├── services/             # Business logic
 ├── models/schemas.py     # Request/response models
 └── utils/logger.py       # Custom logger
tests/                     # API tests
.env.example               # Example env file
requirements.txt           # Dependencies
run_local.sh               # Quick start script
```

---

## ✅ Getting Started

### 1️⃣ Clone the repository:
```bash
git clone https://github.com/Phani-G1992/openai-fastapi-starter.git
cd openai-fastapi-starter
```

### 2️⃣ Set up your virtual environment:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables:
```bash
cp .env.example .env
# Add your OpenAI API key in the .env file
```

### 4️⃣ Run the project locally:
```bash
bash run_local.sh
```
Visit [http://localhost:8000/docs](http://localhost:8000/docs) for auto-generated Swagger documentation.

---

## ✅ Example API Usage
**POST** `/api/v1/generate`
```json
{
  "prompt": "Write a motivational quote about learning."
}
```
**Response:**
```json
{
  "response": "The beautiful thing about learning is that no one can take it away from you."
}
```

---

## ✅ To deploy in production:
- Set `APP_ENV=production` and point to your `.env.production` file.
- Use a production server (Gunicorn + Uvicorn workers).

---

## ✅ License
This project is open-source and available under the [MIT License](LICENSE).

---

## ✅ Contributing
Contributions are welcome!  
If you’d like to improve this template, please fork the repository, make your changes, and submit a pull request.

---

## ✅ Connect
Feel free to reach out if you have questions or ideas! 😎
