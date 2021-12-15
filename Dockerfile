#Deriving the latest base image
FROM python:3.7


#Labels as key value pair
LABEL Maintainer="SemmelJochen"


# Any working direcrtory can be chosen as per choice like '/' or '/home' etc
# i have chosen /usr/app/src
WORKDIR /usr/app/

#to COPY the remote file at working directory in container
COPY ./cogs ./cogs
COPY bot.py ./
COPY requirements.txt ./


RUN pip install -r requirements.txt

ENV DISCORD_TOKEN=NzAxNDA0NDc3MDA1MjM0MTk4.Xpw_0g.ElgnYpR9Klo7xzRVHPXy4n3ruRg
#CMD instruction should be used to run the software
#contained by your image, along with any arguments.

CMD [ "python3", "./bot.py"]