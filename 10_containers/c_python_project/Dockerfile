FROM python:slim

RUN mkdir "/project"
COPY . /project
WORKDIR project
RUN pip install --user poetry
ENV PATH="${PATH}:/root/.local/bin"
RUN poetry install
EXPOSE 5000
CMD ["poetry", "run", "python", "-m", "flask", "--app", "example.main", "run"]