from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openai
from fastapi.responses import FileResponse

## Command:
# uvicorn main:app --reload

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

class Prompt(BaseModel):
    prompt: str
    promptType: str

app = FastAPI()

# CORS - Origins
origins = [
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:4173",
    "http://localhost:3000",
]

# CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Check alive
@app.get("/")
async def say_hello():
    return {"response": "hello"}


# Check alive
@app.get("/execute-query/{filename}", response_class=FileResponse)
async def say_hello(filename):
    import query
    print(filename)
    file_path = filename
    return FileResponse(file_path, filename=file_path)


# Build a file
@app.post("/build-script/")
async def create_item(prompt: Prompt):

    # Authorize Open AI
    openai.organization = config("OPEN_AI_ORG")
    openai.api_key = config("OPEN_AI_KEY")

    # Initialize Prompt Structure
    init_prompt = "Write me a python script only providing the code to "
    mid_prompt = ""
    user_prompt = prompt.prompt.replace(".", ",")
    end_prompt = ", any python libraries must be imported, the file must be called savedfile, there should be no text before importing packages"

    # Handle Excel
    if prompt.promptType == "/excel":
        last_saved = "savedfile.xlsx"
        mid_prompt = "create an excel file that "
        user_prompt = user_prompt.replace("/excel", "")

    # Handle Word
    if prompt.promptType == "/word":
        last_saved = "savedfile.docx"
        mid_prompt = "create a word document that "
        user_prompt = user_prompt.replace("/word", "")

    # Handle PDF
    if prompt.promptType == "/pdf":
        last_saved = "savedfile.pdf"
        mid_prompt = "create a pdf document that "
        user_prompt = user_prompt.replace("/pdf", "")

    # Handle Powerpoint
    if prompt.promptType == "/powerpoint":
        last_saved = "savedfile.pptx"
        mid_prompt = "create a powerpoint presentation that "
        user_prompt = user_prompt.replace("/powerpoint", "")

    # Construct full prompt
    full_prompt = init_prompt + mid_prompt + user_prompt + end_prompt
    full_prompt = full_prompt.replace(",,", ",")
    full_prompt = full_prompt.replace("  ", " ")

    print(full_prompt)

    ## Query codex or Davinci
    # Use code-davinci-002 (not optimal)
    # or Use code-davinci-003 (far better at finishing the code)
    query = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        max_tokens=500,
        temperature=0.2
    )

    # Write output to file
    file = open("query.py", "w")
    file.write(query["choices"][0]["text"])
    file.close()

    return prompt
