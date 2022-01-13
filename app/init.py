from db import engine, check_db
from sqlmodel import Session, SQLModel
from models import Affiliations, Authors, PaperAuthorAffiliations, PaperReferences, Papers
import csv
from os import path
import subprocess

check_db()

try:
    SQLModel.metadata.create_all(engine)
except Exception:
    pass

# subprocess.run(["sh", "/app/import.sh"])

# tables = [("Affiliations.txt", Affiliations), ("Authors.txt", Authors), ("Papers.txt", Papers),
#           ("PaperAuthorAffiliations.txt", PaperAuthorAffiliations), ("PaperReferences.txt", PaperReferences)]

# session = Session(engine)

# with Session(engine) as session:
#     for table in tables:
#         fn, model = table
#         print(fn)
#         with open(path.join("/data", fn)) as f:
#             reader = csv.DictReader(f, delimiter='\t', fieldnames=list(
#                 model.__fields__.keys()))
#             for row in reader:
#                 session.add(model(**row))
#                 session.commit()
