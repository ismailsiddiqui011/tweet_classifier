FROM ubuntu/python

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2

COPY requirements.txt /tmp/
RUN pip3 install --upgrade pip && \
    pip3 install -r /tmp/requirements.txt

COPY . .

RUN chmod +x run.sh

EXPOSE 1411

CMD ["sh", "-c", "./run.sh"]