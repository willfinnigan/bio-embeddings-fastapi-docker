from fastapi import FastAPI
import os
import subprocess as sp
import shutil
from typing import Optional
from bio_embeddings.embed import SeqVecEmbedder
from pydantic import BaseModel
import json
from typing import List, Optional

class Sequence(BaseModel):
    seq: str

class Embedding(BaseModel):
    seqvec: List[float] = []

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/seqvec", response_model=Embedding)
def seqvec(seq: Sequence):
    seq_str = dict(seq)['seq']
    try:
        embedder = SeqVecEmbedder()
        em_per_res = embedder.embed(seq_str)
        em_per_prot = embedder.reduce_per_protein(em_per_res)
        return {"seqvec": list(em_per_prot)}

    except:
        return 'Error running embedding'

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=80)