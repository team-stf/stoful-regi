FROM ubuntu:latest
 
LABEL version="2.0" \
      maintainer="eszett design" \
      description="Dockerで構築したJupyterlabからtKinterやopenpyxlなどを操作できるDocker imageとContainerを作成"
 
# TZを設定する adding in Feb. 3 2022
ENV TZ Asia/Tokyo
RUN apt-get update \
    && apt-get install -y tzdata \
    && rm -rf /var/lib/apt/lists/* \
    && echo "${TZ}" > /etc/timezone \
    && rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata
    
ENV DEBIAN_FRONTEND=noninteractive
 
RUN apt-get update && apt-get install -y \
		python3 \
		python3-pip \
		libx11-dev \
		python3-tk
        
RUN pip3 install jupyterlab \
		pillow \
		openpyxl \
		pandas