FROM postgres:latest

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install git -y
RUN apt-get install wget -y
RUN apt-get install unzip -y

RUN python3 -m pip install --upgrade pip

#assumes You have proper zip in working dir
COPY ml-latest.zip .
RUN unzip ml-latest.zip
RUN rm ml-latest.zip

RUN git clone https://github.com/youngdashu/movie_recommendations.git
WORKDIR movie_recommendations
RUN git checkout container_db_init_sql_to_py

RUN pip3 install -r requirements.txt


ENV PYTHONPATH .


CMD ["-p", "5440"]