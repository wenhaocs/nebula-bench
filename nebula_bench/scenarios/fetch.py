# -*- encoding: utf-8 -*-
from nebula_bench.common.base import BaseScenario


class BaseFetchScenario(BaseScenario):
    abstract = True
    nGQL = "fetch prop on Person {} yield properties(vertex)"
    csv_path = "social_network/dynamic/person.csv"
    csv_index = [0]


class FetchOwn(BaseFetchScenario):
    abstract = False
    nGQL = "fetch prop on Person {} yield properties(vertex)"

class Fetch1Step(BaseFetchScenario):
    abstract = False
    nGQL = "GO 1 STEP FROM {} OVER KNOWS YIELD dst(edge) AS d | fetch prop on Person $-.d yield properties(vertex).birthday"
