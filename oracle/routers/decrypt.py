"""Only routes for 8020, you can declare your own routes here for other devices.
You may want to specify the ECID of the device(s).
"""
from fastapi import APIRouter
from fastapi import HTTPException

from oracle.anya import decrypt

router = APIRouter()


@router.get("/decrypt/8020/{kbag}", tags=["decrypt"])
async def decrypt_A12(kbag: str = None):
    """Route to decrypt A12 AP kbag."""
    key = decrypt.decrypt(kbag)
    return {
        "kbag": kbag,
        "key": key,
    }


@router.get("/decrypt/8020/sep/{kbag}", tags=["decrypt"])
async def decrypt_A12(kbag: str = None):
    """Route to decrypt A12 SEP kbag."""
    key = decrypt.decrypt(kbag, do_sep=True)
    return {
        "kbag": kbag,
        "key": key,
    }
