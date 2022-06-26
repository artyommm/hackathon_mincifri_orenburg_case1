SEARCH_PUBLICATIONS = """
    SELECT 
        * 
    FROM 
        "publication" pb
    WHERE 
        pb."id" in (
            SELECT DISTINCT "publication_id" FROM "publication_keyword" pk WHERE pk."keyword_id"=ANY('{keywords}')
        ) AND
        pb."enterprise_id" = {enterprise} AND
        pb."date_of_publication" BETWEEN '{date_from}'::date AND '{date_to}'::date
"""

GET_ALL = """ SELECT * FROM "{}" """
