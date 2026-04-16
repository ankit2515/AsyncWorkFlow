from celery import Celery

app = Celery("tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0")

@app.task
def process_document(doc_id):
    return f"Processed document {doc_id}"
