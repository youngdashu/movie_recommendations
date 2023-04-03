FROM postgres:latest

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install git -y
RUN apt-get install wget -y
RUN apt-get install unzip -y


RUN git clone https://github.com/youngdashu/movie_recommendations.git
WORKDIR movie_recommendations
RUN git checkout finish_parsers

COPY ml-latest.zip .
RUN unzip ml-latest.zip
RUN rm ml-latest.zip

CMD ["-p", "5440"]