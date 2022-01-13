from sqlmodel import Field, Session, SQLModel, create_engine
from tenacity import retry, wait_fixed


engine = create_engine(
    "mysql+pymysql://root:education_uiuc_pwd@db/education_uiuc")


@retry(wait=wait_fixed(2))
def check_db():
    print("check db")
    with Session(engine) as session:
        session.exec("SELECT 1")
