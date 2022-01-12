from typing import Optional
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, create_engine


class Affiliations(SQLModel, table=True):
    AffiliationId: int = Field(default=None, primary_key=True)
    Rank: int
    NormalizedName: str
    DisplayName: str
    GridId: str
    OfficialPage: str
    WikiPage: str
    PaperCount: int
    PaperFamilyCount: int
    CitationCount: int
    Iso3166Code: str
    Latitude: Optional[float]
    Longitude: Optional[float]
    CreatedDate: datetime


class Authors(SQLModel, table=True):
    AuthorId: int = Field(default=None, primary_key=True)
    Rank: int
    NormalizedName: str
    DisplayName: str
    LastKnownAffiliationId: Optional[int]
    PaperCount: int
    PaperFamilyCount: int
    CitationCount: int
    CreatedDate: datetime


class Papers(SQLModel, table=True):
    PaperId: int = Field(default=None, primary_key=True)
    Rank: int
    Doi: str
    DocType: str
    PaperTitle: str
    OriginalTitle: str
    BookTitle: str
    Year: Optional[int]
    Date: Optional[datetime]
    OnlineDate: Optional[datetime]
    Publisher: str
    JournalId: Optional[int]
    ConferenceSeriesId: Optional[int]
    ConferenceInstanceId: Optional[int]
    Volume: str
    Issue: str
    FirstPage: str
    LastPage: str
    ReferenceCount: int
    CitationCount: int
    EstimatedCitation: int
    OriginalVenue: str
    FamilyId: int
    FamilyRank: int
    DocSubTypes: str
    CreatedDate: datetime


class PaperAuthorAffiliations(SQLModel, table=True):
    Id: int = Field(default=None, primary_key=True)
    PaperId: int = Field(default=None, foreign_key="papers.PaperId")
    AuthorId: int = Field(default=None, foreign_key="authors.AuthorId")
    AffiliationId: int = Field(
        default=None, foreign_key="affiliations.AffiliationId")
    AuthorSequenceNumber: int
    OriginalAuthor: str
    OriginalAffiliation: str


class PaperReferences(SQLModel, table=True):
    PaperId: int = Field(
        default=None, foreign_key="papers.PaperId", primary_key=True)
    PaperReferenceId: int = Field(
        default=None, foreign_key="papers.PaperId", primary_key=True)


engine = create_engine(
    "mysql+pymysql://root:education_uiuc_pwd@db/education_uiuc")

SQLModel.metadata.create_all(engine)
