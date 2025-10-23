from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="Use Here Your Api Key")

# Allow requests from React (localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev only use *  — for in production  use http://localhost:3000 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data.get("message")

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_message}]
    )

    return {"reply": response.choices[0].message.content.strip()}
