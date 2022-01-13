LOAD DATA LOCAL INFILE '/data/Affiliations.txt' INTO TABLE affiliations FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/data/Authors.txt' INTO TABLE authors FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/data/Papers.txt' INTO TABLE papers FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
LOAD DATA LOCAL INFILE '/data/PaperAuthorAffiliations.txt' INTO TABLE paperauthoraffiliations FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' (PaperId, AuthorId, AffiliationId, AuthorSequenceNumber, OriginalAuthor, OriginalAffiliation) SET Id = NULL;
LOAD DATA LOCAL INFILE '/data/PaperReferences.txt' INTO TABLE paperreferences FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';
