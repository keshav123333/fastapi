FROM python:3.11-slim


#set working dir
WORKDIR /app

COPY requirement.txt .
RUN pip install --no-cache-dir -r requirement.txt

#copy rest of the code to /app
COPY . .
EXPOSE 8000

CMD ["uvicorn","app:main","--host","0.0.0.0","--port","8000"]

# ise baad $ docker build -t keshavrai2004/insurance . 
#docker images
#docker login 
#docker push keshavrai2004/insurance
#
# bhai iske liye tu chagpt ki file dekh sakta hai 