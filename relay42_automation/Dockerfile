FROM dorowu/ubuntu-desktop-lxde-vnc

RUN sudo apt-get update -y && \
    sudo apt-get install python-pip wget curl -y && \
    sudo pip install --upgrade pip && \
    sudo pip install selenium

ADD https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz ./

RUN tar -zxvf ./geckodriver-v0.20.1-linux64.tar.gz -C /usr/bin

RUN mkdir relay42
COPY ./relay_42 relay42/
WORKDIR relay42
ENTRYPOINT ["sudo", "python", "relay42_main.py"]
~                                                                                                                                                        
~               
