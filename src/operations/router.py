# from datetime import time
import time
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_cache.decorator import cache
from src.database import get_async_session
from src.operations.models import operation
from src.operations.schemas import OperationCreate

# 6 урок 15:00 
router = APIRouter(
    prefix="/operations",
    tags=["Operation"],
)

# 8 урок 8:45
@router.get("/long_operation")
@cache(expire=30)  # время хранения в redis
def get_long_op():
    time.sleep(2)
    return "Много много данных которые долго вычислялись"


@router.get("/")  # создаем endpoint Operations
#  при возврате клиенту какого-то объема страниц отдавать через пагинацию (по 100 или по 1000), а не весь объем.
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    #  всегда оборачивается в try except
    try:
        query = select(operation).where(operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        #  хороший тон записать ошибку в журнал/передать разработчику
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("/")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
