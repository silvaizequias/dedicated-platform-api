from fastapi import FastAPI
from accounts.routes import router as accounts
from evidence.routes import router as evidence
from notes.routes import router as notes
from orders.routes import router as orders
from subscriptions.routes import router as subscriptions
from tasks.routes import router as tasks

app = FastAPI()

app.include_router(accounts, prefix="/accounts", tags=["accounts"])
app.include_router(evidence, prefix="/evidence", tags=["evidence"])
app.include_router(notes, prefix="/notes", tags=["notes"])
app.include_router(orders, prefix="/orders", tags=["orders"])
app.include_router(subscriptions, prefix="/subscriptions", tags=["subscriptions"])
app.include_router(tasks, prefix="/tasks", tags=["tasks"])


@app.on_event("startup")
@app.get("/", tags=["main"])
def main():
    print(f"APP IS RUNNING")
    return {"message": "Dedicated Platform API"}
