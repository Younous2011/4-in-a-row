FROM ubuntu

WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y \
    python3-dev -y \ 
    python3-setuptools -y \ 
    python3-numpy -y \ 
    python3-opengl -y  \ 
    libsdl-imagy \ 
    libsdl-mixer1.2-dev -y
RUN apt-get install -y \
    libsdl-ttf2.0-dev -y \ 
    libsmpeg-dev -y \ 
    libsdl1.2-dev -y \ 
    libportmidi-dev -y \ 
    libswscale-dev -y \ 
    libavformat-dev -y \ 
    libavcodec-dev -y \ 
    libtiff5-dev -y \ 
    libx11-6 -y \ 
    libx11-dev -y \ 
    fluid-soundfont-gm -y \ 
    timgm6mb-soundfont -y \ 
    xfonts-base -y \ 
    xfonts-100dpi -y \ 
    xfonts-75dpi -y \ 
    xfonts-cyrillic -y \ 
    fontconfig -y \ 
    fonts-freefont-ttf -y \ 
    libfreetype6-dev -y 

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "main.py"]