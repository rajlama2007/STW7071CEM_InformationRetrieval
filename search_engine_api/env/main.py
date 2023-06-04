from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

# Get the absolute path to the directory containing the module
module_path = os.path.abspath("C:\\Users\\Asus\\Downloads\\STW7071CEM_Information_Retrieval-master\\STW7071CEM_Information_Retrieval-master\\search_engine_api\\env")

# Add the module path to sys.path
sys.path.append(module_path)
from SearchEngine import search
app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:3001",
    # Add more origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Project": "Information Retrieval"}

@app.get("/search")
def read_item(query='',page: int = 1, size: int = 30):
    try:
        result = search(query=query)
        pagination = slice((page*size)-size, page*size)
        paginate_data = result['data'][pagination]
        print("result", len(paginate_data))
        return {
            "results":paginate_data,
            'page':page,
            'size':size,
            'totalData': result['totalData']
        }
    except:
        return {"error": "error"}