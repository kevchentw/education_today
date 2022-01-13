from flask import Flask, jsonify, request
import models
from db import engine
from sqlmodel import Session, select, func

app = Flask(__name__)


@app.route("/api/most-cited-papers", methods=["GET"])
def most_cited_papers():
    args = request.args
    authorId = int(args.get('authorId', "2096520082"))
    limit = int(args.get('limit', "10"))
    with Session(engine) as session:
        authorData = session.exec(select(models.Authors).where(
            models.Authors.AuthorId == authorId)).first().dict()
        q_author_papers = select(models.PaperAuthorAffiliations.PaperId).where(
            models.PaperAuthorAffiliations.AuthorId == authorId)
        q = select(models.PaperReferences.PaperReferenceId, func.count(1)).where(models.PaperReferences.PaperId.in_(
            q_author_papers)).group_by(models.PaperReferences.PaperReferenceId).order_by(func.count(1).desc()).limit(limit)
        paper_cited_cnt = session.exec(q).all()
        paper_cited_cnt_map = {x[0]: x[1] for x in paper_cited_cnt}
        paper_cited_ids = list(paper_cited_cnt_map.keys())
        papers = session.exec(select(models.Papers).where(
            models.Papers.PaperId.in_(paper_cited_ids)))
        results = []
        for paper in papers.all():
            results.append(
                {**dict(paper.dict()), "CitedByCount": paper_cited_cnt_map[paper.PaperId]})
        results.sort(key=lambda x: -x["CitedByCount"])
        return jsonify({
            "results": results,
            "author": authorData
        })


@app.route("/api/most-related-insitutions", methods=["GET"])
def most_related_insitutions():
    args = request.args
    affiliationId = int(args.get('affiliationId', "162714631"))
    limit = int(args.get('limit', "10"))
    with Session(engine) as session:
        affiliationData = session.exec(select(models.Affiliations).where(
            models.Affiliations.AffiliationId == affiliationId)).first().dict()
        q_affiliation_author = select(models.Authors.AuthorId).where(
            models.Authors.LastKnownAffiliationId == affiliationId).distinct()
        q_co_author_paper = select(models.PaperAuthorAffiliations.PaperId).where(
            models.PaperAuthorAffiliations.AuthorId.in_(q_affiliation_author)).distinct()
        q_co_author = select(models.PaperAuthorAffiliations.AuthorId).where(
            models.PaperAuthorAffiliations.PaperId.in_(q_co_author_paper)).where(~models.PaperAuthorAffiliations.AffiliationId.in_([affiliationId])).distinct()
        q_affiliation = select(models.Authors.LastKnownAffiliationId, func.count(1)).where(models.Authors.AuthorId.in_(
            q_co_author)).where(~models.Authors.LastKnownAffiliationId.in_([0, affiliationId])).group_by(models.Authors.LastKnownAffiliationId).order_by(func.count(1).desc()).limit(limit)
        related_affiliations = session.exec(q_affiliation).all()
        related_affiliations_map = {x[0]: x[1] for x in related_affiliations}
        related_affiliation_ids = list(related_affiliations_map.keys())
        affiliations = session.exec(select(models.Affiliations).where(
            models.Affiliations.AffiliationId.in_(related_affiliation_ids))).all()
        results = []
        for affiliation in affiliations:
            results.append({**dict(affiliation.dict()),
                           "RelatedCount": related_affiliations_map[affiliation.AffiliationId]})
        results.sort(key=lambda x: -x["RelatedCount"])
        return jsonify({
            "results": results,
            "affiliation": affiliationData
        })
