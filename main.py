from fastapi import FastAPI
import os
import subprocess as sp
import shutil
from typing import Optional
from bio_embeddings.embed import SeqVecEmbedder

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/seqvec")
def seqvec(sequence: str):
    try:
        embedder = SeqVecEmbedder()
        em_per_res = embedder.embed(sequence)
        em_per_prot = embedder.reduce_per_protein(em_per_res)
        return em_per_prot
    except:
        return 'Error running embedding'