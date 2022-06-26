SEARCH_PUBLICATIONS = """
    SELECT 
        pb."id",
        pb."title",
        to_char(pb."date_of_publication", 'dd-mm-yyyy'),
        pb."publication_url",
        en."name",
        ir."name"
    FROM 
        "publication" pb
        JOIN "enterprise" en ON pb."enterprise_id" = en."id"
        JOIN "informationresource" ir ON pb."informationResource_id" = ir."id"
    WHERE 
        pb."id" in (
            SELECT DISTINCT "publication_id" FROM "publication_keyword" pk WHERE pk."keyword_id"=ANY('{keywords}')
        ) AND
        pb."enterprise_id" = {enterprise} AND
        pb."date_of_publication" BETWEEN '{date_from}'::date AND '{date_to}'::date
"""

GET_ALL = """ SELECT * FROM "{}" """
