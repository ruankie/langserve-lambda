FROM amazon/aws-lambda-python:3.11

RUN pip install poetry==1.6.1

RUN poetry config virtualenvs.create false

WORKDIR ${LAMBDA_TASK_ROOT}

COPY ./pyproject.toml ./README.md ./poetry.lock* ./

RUN poetry install  --no-interaction --no-ansi --no-root

COPY ./app ./app

RUN poetry install --no-interaction --no-ansi

CMD [ "app.server.handler" ]
