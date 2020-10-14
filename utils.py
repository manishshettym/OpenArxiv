import arxiv
import requests
import json
import pandas as pd

def get_papers_and_code(query, total):
    max_count=50
    start_index = 0
    total_reqd_count = total
    total_paper_count = 0

    titles = []
    code_links = []

    while(total_paper_count < total_reqd_count):
        res_paper = arxiv.query(query=query, start=start_index, max_results=max_count, sort_by="lastUpdatedDate")

        for paper in res_paper:
            paper_title = paper['title'].replace("\n", '')
            paper_id = paper['id'].lstrip("http://arxiv.org/abs/")

            apwk_link = f"https://arxiv.paperswithcode.com/api/v0/papers/{paper_id}"
            res_code = json.loads(requests.get(url=apwk_link).text)
            if('detail' in res_code.keys() and 'is not found' in res_code["detail"]):
                continue

            if(res_code["unofficial_count"]>0):
                total_paper_count+=1
                if(total_paper_count < total_reqd_count):
                    print(paper_title)
                    print(res_code["paper_url"])
                    print()

                    titles.append(paper_title)
                    code_links.append(res_code["paper_url"])

        start_index+=max_count

    df = pd.DataFrame({"Title":titles, "Links":code_links})
    df.reset_index(drop=True, inplace=True)
    return df