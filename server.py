from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI

app = FastAPI()
client = OpenAI(api_key="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")

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
