FROM python

# set the working directory in the container
WORKDIR /code

# copy requirements.txt to the working directory
COPY requirements.txt .

# install dependecies
RUN pip install -r requirements.txt

# copy content of the local src directory to the working directory
COPY src/ .

# command to run on container start
RUN ["python", "./app.py"]