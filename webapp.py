from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import threading
import os
import uvicorn

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Answer(BaseModel):
    answer: str


answer = "No incoming answers"


@app.post("/api/answers")
async def post_data(request_data: Answer):
    global answer
    answer = request_data.answer
    return {"status": "success", "data": answer}


# @app.put('/api/answers')
# async def put_requests():
#     answers.clear()


@app.get('/api/answers')
def get_requests():
    return answer


def run_streamlit():
    os.system('streamlit run ./streamlit_app.py --server.port 8501')


if __name__ == '__main__':
    threading.Thread(target=run_streamlit).start()
    uvicorn.run(app, host="0.0.0.0", port=8000)
