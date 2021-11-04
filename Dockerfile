FROM continuumio/miniconda3:4.8.2

RUN conda install -c conda-forge jsonnet
RUN conda install pandas
RUN conda install scikit-learn
RUN pip install bio-embeddings[seqvec]
RUN pip install fastapi uvicorn python-multipart

EXPOSE 80

COPY ./main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]