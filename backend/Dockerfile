FROM python:3.6

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN apt-get update && apt-get install -y libgdal-dev gcc
RUN pip install "gdal==2.3.0" --global-option=build_ext --global-option="-I/usr/include/gdal/"

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Force the binary layer of the stdout and stderr streams (which is available as their buffer attribute) to be unbuffered. The text I/O layer will still be line-buffered if writing to the console, or block-buffered if redirected to a non-interactive file.
# PYTHONUNBUFFERED=true
# If this is set before running the interpreter, it overrides the encoding used for stdin/stdout/stderr, in the syntax encodingname:errorhandler. Both the encodingname and the :errorhandler parts are optional and have the same meaning as in str.encode().
# PYTHONIOENCODING='utf-8'
ENV PYTHONUNBUFFERED=true PYTHONIOENCODING=utf-8 PYTHONHASHSEED=random PYTHONDONTWRITEBYTECODE=true

ENTRYPOINT ["dockerize", "-wait", "tcp://db:5432", "-timeout", "30s"]

WORKDIR /app
ADD . /app
