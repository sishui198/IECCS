import json
import sys
sys.path.insert(0, "/Users/petterasla/Desktop/Skole/9. semester/In-Depth project/IECCS/Information Retrieval/retrieval/retrieval/spiders")
import import_data

def compareData():
    articleInfo = import_data.getArticleInfo("tcp_articles.txt")

    with open("retrieval/retrieval/spiders/meta.json") as metaJson:
        metaInfo = json.load(metaJson)
        metaJson.close()

    titleArticle = articleInfo[0][2].lower().strip()
    titleMeta = metaInfo[0]["message"]["items"][0]["title"][0].lower().strip()

    yearArticle = str(articleInfo[0][1]).strip()
    yearMeta = str(metaInfo[0]["message"]["items"][0]["issued"]["date-parts"][0][0]).strip()

    info = []
    for article in articleInfo:
        articleDict = {}
        status = {}
        for meta in metaInfo:
            if (article[2]!= meta["message"]["query"]["search-terms"]):
                continue
            else:
                #print "Same article title and search terms in meta"
                articleTitle = article[2].lower().strip()
                articleYear = str(article[1].lower().strip())
                try:
                    metaTitle = meta["message"]["items"][0]["title"][0].lower().strip()
                except:
                    pass
                try:
                    metaYear = str(meta["message"]["items"][0]["issued"]["date-parts"][0][0]).strip()
                except:
                    pass
                try:
                    metaPublisher = meta["message"]["items"][0]["publisher"]
                except:
                    pass
                try:
                    metaDOI = meta["message"]["items"][0]["DOI"]
                except:
                    pass
                try:
                    metaOriginURL = meta["message"]["items"][0]["URL"]
                except:
                    pass
                try:
                    metaISSN = meta["message"]["items"][0]["ISSN"]
                except:
                    pass
                try:
                    metaSubject = meta["message"]["items"][0]["subject"]
                except:
                    pass
                try:
                    metaType = meta["message"]["items"][0]["type"]
                except:
                    pass

                metaAuthor = []
                try:
                    for author in meta["message"]["items"][0]["author"]:
                        metaAuthorDict = {}
                        try:
                            firstName = author["given"].encode('ascii', 'ignore')
                            metaAuthorDict["First name"] = firstName
                        except:
                            pass
                        try:
                            metaAuthorDict["Last name"] = author["family"].encode('ascii', 'ignore')
                            metaAuthor.append(metaAuthorDict)
                        except:
                            pass
                except:
                    pass

                """print "comparing this info: "
                print articleTitle
                print metaTitle
                print articleYear
                print metaYear
                print "\n"
                """

                articleDict["Title"] = str(articleTitle)
                articleDict["Year"] = str(articleYear)
                status["isMetaTitleEqualToOriginal"] = "False"
                status["isMetaYearEqualToOriginal"] = "True"


                if (articleTitle == metaTitle):
                    #print "title is the same --> put into same shit!"

                    articleDict["Publisher"] = str(metaPublisher)
                    articleDict["DOI"] = str(metaDOI)
                    articleDict["OriginURL"] = str(metaOriginURL)
                    articleDict["Author"] = metaAuthor
                    articleDict["ISSN"] = metaISSN
                    articleDict["Subject"] = metaSubject
                    articleDict["Type"] = str(metaType)
                    status["isMetaTitleEqualToOriginal"] = "True"
                    if (articleYear != metaYear):
                        status["isMetaYearEqualToOriginal"] = "False"
                else:
                    #print "DIFFERENT TITLES"
                    articleDict["Meta title"] = metaTitle.encode('ascii', 'ignore')

                articleDict["Status"] = status
                info.append(articleDict)
                metaInfo.remove(meta)
                break


    print "finished with meta data comparison"
    return info

def addAbstractToData(info):
    with open("retrieval/retrieval/spiders/abstracts.json") as metaJson:
        abstracts = json.load(metaJson)
        metaJson.close()

    #print abstracts[0]
    title1 = abstracts[0]["title"]
    title2 = info[0]["Title"]

    print "\n\n Adding abstracts..."

    for x in info:
        for abstract in abstracts:
            title = abstract["title"].lower()

            x["Status"]["isAbstractTitleEqualToOriginal"] = "False"
            if (x["Title"] != title):
                continue
            else:
                x["URL"] = abstract["url"].encode('ascii', 'ignore')
                x["Abstract"] = abstract["abstract"][0].encode('ascii', 'ignore')
                x["Status"]["isAbstractTitleEqualToOriginal"] = "True"
                break

    print "finished adding abstracts"
    return info


def findAbstractAbsence(info):
    print "size of info: " + str(len(info))
    counter = 0
    for x in info:
        if (x["Status"]["isAbstractTitleEqualToOriginal"] == "True" and x["Abstract"] == "[No abstract available]"):
            print x
            counter += 1
    print "number of missing abstracts is " + str(counter)

info = compareData()
inf = addAbstractToData(info)
findAbstractAbsence(inf)