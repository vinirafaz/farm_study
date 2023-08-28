from fastapi import APIRouter
from . import auth_route


router = APIRouter(prefix="/api", tags=["api"])

router.include_router(auth_route.auth, tags=["auth"])
