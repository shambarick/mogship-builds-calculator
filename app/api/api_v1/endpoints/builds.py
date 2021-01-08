from typing import Optional

from fastapi import APIRouter, Query

from app.core.es import get_client


router = APIRouter()


@router.get("")
async def get_builds(
    hulls: Optional[str] = Query(None),
    sterns: Optional[str] = Query(None),
    bows: Optional[str] = Query(None),
    bridges: Optional[str] = Query(None),
    surveillance: Optional[str] = Query(None),
    retrieval: Optional[str] = Query(None),
    speed: Optional[str] = Query(None),
    range: Optional[str] = Query(None),
    favor: Optional[str] = Query(None),
    sort: Optional[str] = Query(None),
):
    query = {
            "size": 100,
            "query": {
                "bool": {
                    "filter": [
                        {
                            "terms": {
                                "Slots.Hull": [23, 27],
                            },
                        },
                        {
                            "range": {
                                "Rank": {
                                    "lte": 10,
                                },
                            },
                        },
                    ],
                },
            },
            "sort": [
                {
                    "Stats.Speed": {
                        "order": "DESC"
                    },
                },
            ]
    }

    results = await get_client().search(
        index="submarinebuilds-*",
        body=query,
    )
    hits = [r["_source"] for r in results["hits"]["hits"]]

    return hits
