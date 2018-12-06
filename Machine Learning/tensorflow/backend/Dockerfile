FROM tensorflow/tensorflow
ENV FLASK_DEBUG=1
COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y python-tk
COPY . .
