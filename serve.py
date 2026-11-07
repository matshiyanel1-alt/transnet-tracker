import modal
from pathlib import Path

image = modal.Image.debian_slim().pip_install("fastapi[standard]")
app = modal.App("transnet-demo")

HTML = (Path(__file__).parent / "index.html").read_text()

@app.function(image=image)
@modal.fastapi_endpoint(method="GET")
def serve():
    from fastapi.responses import HTMLResponse
    return HTMLResponse(HTML)
