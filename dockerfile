#Repo Clonning ⚡♥️
RUN git clone https://github.com/Team-Mafia/spambot /root/userbot

RUN mkdir /root/userbot/bin/

WORKDIR /root/userbot/

RUN chmod +x /usr/local/bin/

*RUN pip install -r requirements.txt

CMD ["bash","./EAGLEMAFIA-USPAMBOT/start.sh"]
