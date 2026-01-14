
import inspect
from SampleFile import get_query_tag



class cdmExtractionService:
    def __init__(self, dim_abr,cycle_date,source_dtl):
        self.dim_abr = dim_abr
        self.cycle_date = cycle_date
        self.source_dtl = source_dtl

    def extraction(self):
        query_tag1 = get_query_tag()
        print(query_tag1)
        query_tag2 = get_query_tag()
        print(query_tag2)
        return ""

if __name__ == '__main__':
    dim_abr = 'mkrt'
    cycle_date = '2025-12-30'
    source_dtl = 'od-source-dtl'
    cdm = cdmExtractionService(dim_abr,cycle_date,source_dtl)
    res = cdm.extraction()