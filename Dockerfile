FROM python:3.8

ADD pca_project.py .

RUN pip install PyQt5 pandas matplotlib sklearn

CMD [ "python", "./pca_project.py"]