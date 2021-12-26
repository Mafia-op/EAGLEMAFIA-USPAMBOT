RUN git clone https://github.com/Team-Mafia/spambot /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN chmod +x /usr/local/bin/*
RUN pip3 install -r requirements.txt
CMD ["bash","./EAGLEMAFIA-USPAMBOT/start.sh"]

#Repo Clonning ⚡♥️
RUN git clone https://github.com/Team-mafia/spambot.git /root/userbot

#working directory 
WORKDIR /root/userbot

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/userbot/bin:$PATH"

CMD ["python3","-m","userbot"]
