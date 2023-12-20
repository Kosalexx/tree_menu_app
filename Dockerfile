FROM python:3.10

WORKDIR /project

COPY requirements.txt /project/requirements.txt

RUN apt-get update \
  && apt-get install -y build-essential \
  && apt-get install -y gettext \
  && pip install --no-cache-dir --upgrade -r /project/requirements.txt \
  && pip install gunicorn

COPY . /project

RUN chmod +x ./src/tree_menu_app/start_app.sh

CMD ["./src/tree_menu_app/start_app.sh"] 
