from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="Practice Login Dashboard")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

# Demo-only credentials. Never store real passwords like this.
DEMO_USERNAME = "admin"
DEMO_PASSWORD = "admin123"
active_sessions: set[str] = set()


@app.get("/", response_class=HTMLResponse)
async def login_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": None},
    )


@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == DEMO_USERNAME and password == DEMO_PASSWORD:
        active_sessions.add(username)
        response = RedirectResponse(url="/dashboard", status_code=303)
        response.set_cookie("demo_user", username, httponly=True, samesite="lax")
        return response

    return templates.TemplateResponse(
        request=request,
        name="login.html",
        context={"error": "Invalid username or password."},
        status_code=401,
    )


@app.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request):
    username = request.cookies.get("demo_user")
    if username not in active_sessions:
        return RedirectResponse(url="/", status_code=303)

    return templates.TemplateResponse(
        request=request,
        name="dashboard.html",
        context={"username": username},
    )


@app.post("/logout")
async def logout(request: Request):
    username = request.cookies.get("demo_user")
    if username:
        active_sessions.discard(username)
    response = RedirectResponse(url="/", status_code=303)
    response.delete_cookie("demo_user")
    return response
