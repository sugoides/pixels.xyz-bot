FROM python:latest

ARG secret=default_value
ARG tgID=default_value
# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app


CMD [ "python", "bot.py ${secret} ${tgID}", ]