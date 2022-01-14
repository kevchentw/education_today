# Education Today

by: Kuan-Yin Chen (kuanyin2)

Video: https://www.youtube.com/watch?v=BrgfgPu6jhQ

## Tasks' Methodology

### Task 1: Most Cited Paper

1. Find author's all papers 
```
q_author_papers = select(models.PaperAuthorAffiliations.PaperId).where(models.PaperAuthorAffiliations.AuthorId == authorId)
```


2. 
- Get all referenced papers from first step's papers.
- Aggreated and count number of been referenced 
- Order and limit the result
```
q = select(models.PaperReferences.PaperReferenceId, func.count(1)).where(models.PaperReferences.PaperId.in_(q_author_papers)).group_by(models.PaperReferences.PaperReferenceId).order_by(func.count(1).desc()).limit(limit)
```

### Task 2: Most Related Insitutions

1. Find affiliation's all authors
```
q_affiliation_author = select(models.Authors.AuthorId).where(models.Authors.LastKnownAffiliationId == affiliationId).distinct()
```

2. Find all papers from step one's authors
```
q_co_author_paper = select(models.PaperAuthorAffiliations.PaperId).where(models.PaperAuthorAffiliations.AuthorId.in_(q_affiliation_author)).distinct()
```

3. Find all co-authors from second step's paper (exclude input affiliationId)
```
q_co_author = select(models.PaperAuthorAffiliations.AuthorId).where(models.PaperAuthorAffiliations.PaperId.in_(q_co_author_paper)).where(~models.PaperAuthorAffiliations.AffiliationId.in_([affiliationId])).distinct()
```

4. 
- Get third step's authors LastKnownAffiliationId
- Aggreated and count number of LastKnownAffiliationId
- Order and limit the result
```
q_affiliation = select(models.Authors.LastKnownAffiliationId, func.count(1)).where(models.Authors.AuthorId.in_(q_co_author)).where(~models.Authors.LastKnownAffiliationId.in_([0, affiliationId])).group_by(models.Authors.LastKnownAffiliationId).order_by(func.count(1).desc()).limit(limit)
```

## Development Setup

### Requirements

1. Docker
2. Node.js + yarn
3. Python 3.9

### Steps

#### Backend + Database + Data Import

1. Unzip data.zip as `data/` in project's root folder
2. `docker-compose up`

#### Frontend

1. `cd frontend`
2. `yarn install`
3. `yarn start`
4. open `http://localhost:3000/`

## System Methodology

### Database Design

1. Database schema is based on https://docs.microsoft.com/en-us/academic-services/graph/reference-data-schema
2. Foreign Keys and Indexs are added to improve query perfomance

code: `app/models.py`

p.s
I added an addition `Id` column as primary key on table `PaperAuthorAffiliations`, because the documents says that "It is possible to have multiple rows with same (PaperId, AuthorId, AffiliationId) when an author is associated with multiple affiliations."

### Database initialization

Use SQLModel (sqlalchemy) to init database: `SQLModel.metadata.create_all(engine)`

code: `app/init.py`

### Data Import

Import data using MySQL's `LOAD DATA` statement for better performance since the dataset is large

code: `app/import.sql`

### Frontend

#### Modules

1. React Base: [create-react-app](https://github.com/facebook/create-react-app)
2. UI Framework: [Chakra Ui](https://chakra-ui.com/)
3. Request: [Axios](https://github.com/axios/axios)
4. TypeScript

#### Types

API data schema: `frontend/src/types`

#### Components

1. Task 1:  `frontend/src/components/MostCitedPapers.tsx`
2. Task 2: `frontend/src/components/MostRelatedInsitutions.tsx`

#### State Management

I use hook (`useState`) to store form value and api response.

### Backend

#### Modules

1. Backend: [Flask](https://github.com/pallets/flask)
2. ORM: [SqlModel](https://sqlmodel.tiangolo.com/)
3. SQL Connector: [pymysql](https://github.com/PyMySQL/PyMySQL)
4. Retry: [tenacity](https://github.com/jd/tenacity)

#### API Endpoints

code: `app/app.py`

