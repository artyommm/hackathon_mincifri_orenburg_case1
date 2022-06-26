SEARCH_PUBLICATIONS = """
    SELECT 
        pb."id",
        pb."title",
        to_char(pb."date_of_publication", 'dd-mm-yyyy'),
        pb."publication_url",
        en."name",
        pb."information_resource",
        kw."name"
    FROM 
        "publication" pb
        JOIN "enterprise" en ON pb."enterprise_id" = en."id"
        JOIN "keyword" kw ON pb."keyWord_id" = kw."id"
    WHERE 
        pb."keyWord_id" = {keyword} AND
        pb."enterprise_id" = {enterprise} AND
        pb."date_of_publication" BETWEEN '{date_from}'::date AND '{date_to}'::date
"""

GET_ALL = """ SELECT * FROM "{}" """

SEARCH_ALL_PUBLICATIONS = """
    SELECT 
        pb."id",
        en."name",
        pb."information_resource",
        pb."title",
        to_char(pb."date_of_publication", 'dd-mm-yyyy'),
        pb."publication_url",
        kw."name"
    FROM 
        "publication" pb
        JOIN "enterprise" en ON pb."enterprise_id" = en."id"
        JOIN "keyword" kw ON pb."keyWord_id" = kw."id"
"""
