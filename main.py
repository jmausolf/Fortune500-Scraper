import json
import httplib2


h = httplib2.Http(".cache")

with open('fortune500-list.txt', 'w') as f:
    i = 0

    while i < 500:
        (resp_headers, content) = h.request("http://fortune.com/api/v2/list/2013055/expand/item/ranking/asc/" + str(i)
                                            + "/100", "GET")

        content = json.loads(content)

        for company in content["list-items"]:
            i += 1
            print "[ " + str(i) + " ] - " + company["title"]

            f.write(("[ " + str(i) + " ] - " + company["title"] + "\n").encode('utf8'))
