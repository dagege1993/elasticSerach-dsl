from datetime import datetime
from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text, connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class Article(DocType):
    title = Text(analyzer='snowball', fields={'raw': Keyword()})  #需要全文搜尋的欄位要設為 analyzed
    body = Text(analyzer='snowball')
    tags = Keyword()
    published_from = Date()
    lines = Integer()

    class Meta:
        index = 'blog'

    def save(self, ** kwargs):
        self.lines = len(self.body.split())
        return super(Article, self).save(** kwargs)

    def is_published(self):
        return datetime.now() > self.published_from

# create the mappings in elasticsearch 这样Elasticsearch才根据Doctype产生对应的mapping
Article.init()

# create and save and article
article = Article(meta={'id': 42}, title='Hello world!', tags=['test'])
article.body = ''' looong text '''
article.published_from = datetime.now()
article.save()

article = Article.get(id=42)
print(article.is_published())

# Display cluster health
print(connections.get_connection().cluster.health())


