import json
import re
import httplib2
import argparse

def remove_non_ascii_2(text, sub=""):
    import re
    return re.sub(r'[^\x00-\x7F]+', sub, text)


def getFortunelist(n=500):

    h = httplib2.Http(".cache")

    with open('fortune{}-list.csv'.format(n), 'w') as f:
        i = 0

        f.write("rank,company\n")

        while i < n:
            (resp_headers, content) = h.request("http://fortune.com/api/v2/list/2013055/expand/item/ranking/asc/" + str(i)
                                                + "/100", "GET")

            content = json.loads(content.decode('utf-8'))

            for company in content["list-items"]:
                i += 1
                print ("[ " + str(i) + " ] - " + company["title"])

                f.write("{},{}\n".format(str(i), remove_non_ascii_2(company["title"].strip(), "'")))




if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--number", default=500, type=int, help="number of companies")
    args = parser.parse_args()

    getFortunelist(args.number)