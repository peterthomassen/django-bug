FROM python:3.7

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		default-mysql-client default-libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3 \
	--no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r requirements.txt && rm -rf /root/.cache/

COPY . /usr/src/app

EXPOSE 8000
CMD ["./entrypoint.sh"]
