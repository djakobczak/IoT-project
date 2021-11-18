from app.api.deps import get_db
from app.crud.crud_users import create_user, get_user
from app.schemas.user import UserCreate
from app.core.settings import settings


db = next(get_db())
if not get_user(db, settings.OPERATOR_USERNAME):
    admin_user = UserCreate(
        username=settings.OPERATOR_USERNAME,
        password=settings.OPERATOR_PASSWORD)
    create_user(db, admin_user)
    print("Admin user created")

if not get_user(db, settings.RASPBERRY_PI_USERNAME):
    rpi_user = UserCreate(
        username=settings.RASPBERRY_PI_USERNAME,
        password=settings.RASPBERRY_PI_PASSWORD)
    create_user(db, rpi_user)
    print("RasberryPI user created")
