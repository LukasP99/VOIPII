FROM python:3.11-bookworm as build-stage

ENV VENV_PATH="/app/venv"

RUN mkdir app
WORKDIR /app
RUN python3 -m venv $VENV_PATH
RUN $VENV_PATH/bin/pip install -U pip setuptools
RUN $VENV_PATH/bin/pip install poetry

ENV PATH="$VENV_PATH/bin:$PATH"

COPY ./ .

RUN poetry install
RUN poetry build


FROM python:3.11-bookworm as production-stage

ARG db_url
ENV DATABASE_URL="$db_url"

ENV VENV_PATH="/app/venv"

RUN mkdir app
WORKDIR /app
RUN python3 -m venv $VENV_PATH
COPY --from=build-stage /app/dist/*.whl /app

RUN $VENV_PATH/bin/pip install /app/*.whl
ENV PATH="$VENV_PATH/bin:$PATH"

# expose port locally, so we can test the container
EXPOSE 8080

CMD ["voip2be"]
