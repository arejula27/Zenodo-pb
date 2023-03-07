FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive


RUN apt update -y
RUN apt upgrade -y
#RUN unminimize -y

RUN apt install zsh  git sudo man    -y
#RUN apt install python3 pip3 -y

RUN apt install software-properties-common -y
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt update -y 


RUN   apt install python3.8 pip -y

RUN ln -s /usr/bin/python3 /usr/bin/python


RUN useradd --create-home --shell /bin/zsh vscode
RUN adduser vscode sudo 

RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers
RUN echo "vscode:vscode" | chpasswd


COPY ./.zshrc /home/vscode