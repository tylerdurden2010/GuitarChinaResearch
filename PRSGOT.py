import os,sys,urllib2,re
prs = re.compile(r'p.?r.?s.?',re.I)
resultfilter = re.compile(r'(?P<tag1>\<em\>.*\<\/em\>\s.*\<span id=".*"\>\<a href\=\")(?P<tag2>thread\-\d.*.html)\"\>(?P<tag3>.*\<\/a>)')
file = open("c:\\result.txt",'ab')
#f = """GET /forum-100-5.html HTTP/1.1
for i in range(1,100):
    req = urllib2.Request("http://bbs.guitarchina.com/forum-100-"+str(i)+".html")
    req.add_header("Host"," bbs.guitarchina.com")
    req.add_header("User-agent","Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0")
    req.add_header("Referer"," http://bbs.guitarchina.com/forum-100-2.html")
    #req.add_header("Cookie","cdb_sid=x3PVwJ; cdb_smile=2DD0D1; cdb_visitedfid=100D102D42D19D54D101D94D3D118D105; __utma=201140605.1238862654.1365663268.1367040916.1367045568.20; __utmz=201140605.1367040916.19.9.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=polytune%20mini%20%E4%BE%9B%E7%94%B5; cdb_cookietime=2592000; cdb_auth=706ch42cqf%2Fn0yDjNZLDUQ4VIPhH8Ungst9MUkLp%2FZWaMGIYcMQdrvtGNylRIkcbPHIZtiX6wnegwSw%2BrGIsFNeUVWKetA; __utmc=201140605; cdb_oldtopics=D1553451D1553316D1553300D1553429D1553419D1553347D1553361D1553358D; cdb_fid102=1367041597; __utmb=201140605.12.10.1367045568; cdb_fid100=1367046097; checkpm=1")
    req.add_header("Connection","close")
    r = urllib2.urlopen(req)
    line = r.readline()
    while line:
        line = r.readline()
        Match = re.findall(prs,line)
        if Match:
            tmp = line
            Mat = re.search(resultfilter,tmp)
            if Mat:
                url = "http://bbs.guitarchina.com/"+Mat.group('tag2')+"    "+Mat.group('tag3')+"\n"
                #print url
                file.write(url)
            



