from fastapi import FastAPI, HTTPException
from app.controllers.pagamento_controller import router as pagamento_router


app = FastAPI()

app.include_router(pagamento_router)
