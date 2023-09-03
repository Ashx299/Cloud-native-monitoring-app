#use the official python image as the base image
FROM python:3.9-slim-buster

#set the working directory in the container
WORKDIR /app

#copy the requirement files to the working directory
COPY requirements.txt .

#install the required python packages
RUN pip3 install --no-cache-dir -r requirements.txt

#copy the application code to the working directory
COPY . .   

#set the environment variables for the flask app
ENV FLASK_RUN_HOST=0.0.0.0  

#export the port on which the flask app will run
EXPOSE 5000

#start the flask app when the container is run
CMD ["flask", "run"]