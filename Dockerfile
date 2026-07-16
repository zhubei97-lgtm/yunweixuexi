FROM python:3.9-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir flask -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 5000

CMD ["python", "app.py"]
