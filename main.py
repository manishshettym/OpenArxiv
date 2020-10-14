import pandas as pd
from utils import get_papers_and_code

if __name__ == "__main__":
    query = "(cat:cs.SE OR cs.PL) AND (cat:cs.CL OR cat:cs.LG OR cs.AI OR stat.ML)"
    df = get_papers_and_code(query, total=30)
    df.to_excel("Output.xlsx")