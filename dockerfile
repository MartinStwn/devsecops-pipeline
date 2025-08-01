FROM python:3.9-slim
	WORKDIR /app
	COPY requiretments.txt .
	RUN pip install -r
	requiretments.txt
	COPY app.py
	EXPOSE 5000
	CMD ["python", "app.py"]
