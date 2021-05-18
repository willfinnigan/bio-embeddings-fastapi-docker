FROM continuumio/miniconda3:4.8.2

RUN conda install -c conda-forge jsonnet

RUN pip install bio-embeddings-allennlp==0.9.2
RUN pip install boto3==1.17.74
RUN pip install botocore==1.20.74
RUN pip install bio-embeddings==0.1.6
RUN pip install fastapi uvicorn python-multipart

EXPOSE 80

COPY ./main.py main.py

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]