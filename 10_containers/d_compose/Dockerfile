FROM python:slim

RUN mkdir "/project"
COPY . /project
WORKDIR project
RUN pip install --user poetry
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install
EXPOSE 5000
CMD ["poetry", "run", "python", "-m", "flask", "--app", "app", "run"]