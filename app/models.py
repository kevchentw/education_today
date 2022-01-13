from typing import Optional
from datetime import date
from sqlmodel import Field, SQLModel, Column, BigInteger


class Affiliations(SQLModel, table=True):
    __tablename__ = 'affiliations'
    AffiliationId: int = Field(
        default=None, sa_column=Column(BigInteger(), primary_key=True))
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
    CreatedDate: Optional[date]


class Authors(SQLModel, table=True):
    __tablename__ = 'authors'
    AuthorId: int = Field(default=None,
                          sa_column=Column(BigInteger(), primary_key=True))
    Rank: int
    NormalizedName: str
    DisplayName: str
    LastKnownAffiliationId: Optional[int] = Field(default=None,
                                                  sa_column=Column(BigInteger(), index=True))
    PaperCount: int
    PaperFamilyCount: int
    CitationCount: int
    CreatedDate: Optional[date]


class Papers(SQLModel, table=True):
    __tablename__ = 'papers'
    PaperId: int = Field(default=None,
                         sa_column=Column(BigInteger(), primary_key=True))
    Rank: int
    Doi: str
    DocType: str
    PaperTitle: str
    OriginalTitle: str
    BookTitle: str
    Year: Optional[int]
    Date: Optional[date]
    OnlineDate: Optional[date]
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
    CreatedDate: Optional[date]


class PaperAuthorAffiliations(SQLModel, table=True):
    __tablename__ = 'paperauthoraffiliations'
    Id: int = Field(default=None,
                    sa_column=Column(BigInteger(), primary_key=True))
    PaperId: int = Field(
        default=None, foreign_key="papers.PaperId", sa_column=Column(BigInteger(), index=True))
    AuthorId: int = Field(
        default=None, foreign_key="authors.AuthorId", sa_column=Column(BigInteger(), index=True))
    AffiliationId: int = Field(
        default=None, foreign_key="affiliations.AffiliationId", sa_column=Column(BigInteger(), index=True))
    AuthorSequenceNumber: int
    OriginalAuthor: str
    OriginalAffiliation: str


class PaperReferences(SQLModel, table=True):
    __tablename__ = 'paperreferences'
    PaperId: int = Field(
        default=None, foreign_key="papers.PaperId", sa_column=Column(BigInteger(), primary_key=True, index=True))
    PaperReferenceId: int = Field(
        default=None, foreign_key="papers.PaperId", sa_column=Column(BigInteger(), primary_key=True, index=True))
