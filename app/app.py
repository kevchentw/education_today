from flask import Flask, jsonify, request
import models
from db import engine
from sqlmodel import Field, Session, SQLModel, create_engine, select, func

app = Flask(__name__)


@app.route("/api/most-cited-papers", methods=["GET"])
def most_cited_papers():
    args = request.args
    authorId = int(args.get('authorId', "2096520082"))
    limit = int(args.get('limit', "10"))
    with Session(engine) as session:
        paper_cited_cnt = session.exec(select(models.PaperReferences.PaperReferenceId, func.count(1)).where(models.PaperReferences.PaperId.in_(select(
            models.PaperAuthorAffiliations.PaperId).where(models.PaperAuthorAffiliations.AuthorId == authorId))).group_by(models.PaperReferences.PaperReferenceId).order_by(func.count(1).desc()).limit(limit)).all()
        paper_cited_cnt_map = {x[0]: x[1] for x in paper_cited_cnt}
        paper_cited_ids = list(paper_cited_cnt_map.keys())
        papers = session.exec(select(models.Papers).where(
            models.Papers.PaperId.in_(paper_cited_ids)))
        results = []
        for paper in papers.all():
            results.append(
                {**dict(paper.dict()), "CitedByCount": paper_cited_cnt_map[paper.PaperId]})
        results.sort(key=lambda x: -x["CitedByCount"])
        return jsonify(results)
