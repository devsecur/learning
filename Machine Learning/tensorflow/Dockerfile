FROM tensorflow/tensorflow
COPY requirements.txt ./
RUN pip install --upgrade --no-cache-dir -r requirements.txt
RUN apt-get update && apt-get install -y python-tk
COPY . .
CMD [ "python", "./start.py" ]
