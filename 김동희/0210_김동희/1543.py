docs = list(input())
doc = input()
cnt = 0
while len(docs) >= len(doc):
    doc_doc = ''
    for i in range(len(doc)):
        doc_doc += docs[i]
    if doc == doc_doc:
        cnt += 1
        for i in range(len(doc)):
            docs.pop(0)
    else:
        docs.pop(0)
print(cnt)