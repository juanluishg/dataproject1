FROM ubuntu
RUN apt update -y && apt install python3 -y && apt install python3-pip -y
RUN pip3 install psycopg2
RUN apt install wget -y
WORKDIR /
RUN wget https://raw.githubusercontent.com/juanluishg/dataproject1/main/analisis.py
ENTRYPOINT python3 analisis.py
