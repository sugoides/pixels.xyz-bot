FROM python:latest

ARG secret=default_secret_value
ARG tgID=default_tg_id_value

ENV SECRET=$secret
ENV TGID=$tgID
# Create app directory
WORKDIR /app

# Install app dependencies
COPY src/requirements.txt ./

RUN pip install -r requirements.txt

# Bundle app source
COPY src /app


CMD [ 'python', 'bot.py']