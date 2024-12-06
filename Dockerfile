FROM python:latest

RUN useradd -ms /bin/bash evo
USER evo
WORKDIR /home/evo

CMD [ "/bin/bash" ]