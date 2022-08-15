# -*- encoding: utf-8 -*-
from nebula_bench.common.base import BaseScenario


class BaseGoScenario(BaseScenario):
    abstract = True
    nGQL = "MATCH (n:Person)-[:IS_LOCATED_IN]->(p:Place) WHERE id(n)=={} RETURN n.Person.firstName AS firstName, n.Person.lastName AS lastName,n.Person.birthday AS birthday,n.Person.locationIP AS locationIP,n.Person.browserUsed AS browserUsed,id(p) AS cityId,n.Person.gender AS gender,n.Person.creationDate AS creationDate"
    csv_path = "social_network/dynamic/person.csv"
    csv_index = [0]

class MatchSimple(BaseGoScenario):
    nGQL = "MATCH (n:Person) WHERE id(n)=={} RETURN n"
    abstract = False

class Match1(BaseGoScenario):
    nGQL = "MATCH (n:Person)-[:IS_LOCATED_IN]->(p:Place) WHERE id(n)=={} RETURN n.Person.firstName AS firstName, n.Person.lastName AS lastName,n.Person.birthday AS birthday,n.Person.locationIP AS locationIP,n.Person.browserUsed AS browserUsed,id(p) AS cityId,n.Person.gender AS gender,n.Person.creationDate AS creationDate"
    abstract = False

class Match2(BaseGoScenario):
    nGQL = "MATCH (n:Person)<-[:HAS_CREATOR]-(m:`Comment`)-[:REPLY_OF*0..100]->(p:Post) WHERE id(n)=={} MATCH (p)-[:HAS_CREATOR]->(c) RETURN id(m) as messageId, CASE tags(m)[0] WHEN 'Comment' THEN coalesce(m.`Comment`.imageFile,m.`Comment`.content) ELSE coalesce(m.Post.imageFile,m.Post.content) END AS messageContent, CASE tags(m)[0] WHEN 'Comment' THEN m.`Comment`.creationDate ELSE m.Post.creationDate END AS messageCreationDate, id(p) AS originalPostId, id(c) AS originalPostAuthorId, c.Person.firstName as originalPostAuthorFirstName, c.Person.lastName as originalPostAuthorLastName ORDER BY messageCreationDate DESC LIMIT 10"
    abstract = False

class Match3(BaseGoScenario):
    nGQL = "MATCH (n:Person)-[r:KNOWS]-(friend) WHERE id(n) == {} RETURN id(friend) AS personId, friend.Person.firstName AS firstName, friend.Person.lastName AS lastName, r.creationDate AS friendshipCreationDate ORDER BY friendshipCreationDate DESC, personId ASC"
    abstract = False

class complex6(BaseGoScenario):
    nGQL = "GO 1 to 2 steps from {} over KNOWS bidirect where id($$)<>$personId yield distinct id($$) as friend | GO from $-.friend over HAS_CREATOR reversely where $$.Post.content IS NOT EMPTY yield id($$) as friendPost | GO from $-.friendPost over HAS_TAG where $$.`Tag`.name==$tagName yield id($^) as postWithSpecifiedTag | GO from $-.postWithSpecifiedTag over HAS_TAG where $$.`Tag`.name<>$tagName yield properties($$).name as otherTagName, id($^) as commonPost | group by $-.otherTagName yield $-.otherTagName as otherTagName, count($-.commonPost) as postCount | order by $-.postCount desc | limit 10"
    abstract = False
