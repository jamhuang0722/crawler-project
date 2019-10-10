import jieba
import json
from wordcloud import WordCloud
from redis import Redis
from matplotlib import pyplot

s = ['\n', ' ', '导演', '演员', '故事', '电影']
with open('chineseStopWords.txt', encoding='gbk') as f:
    stopwords = {line.strip() for line in f}
    for i in s:
        stopwords.add(i)

redis = Redis('192.168.236.129')
items = redis.lrange('dbreview:items', 0, -1)

words = {}
total = 0
for item in items:
    comment = json.loads(item)
    print(comment)
    cut = jieba.cut(comment['review'])
    for word in cut:
        if word not in stopwords and len(word) != 1:
            words[word] = words.get(word, 0) + 1
            total += 1

freq = {k:round(v/total, 4) for k, v in words.items()}
sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
print(sorted_freq)
wordcloud = WordCloud(width=1920, height=1080, font_path='阿里汉仪智能黑体.ttf',
                      background_color='white', max_font_size=250, margin=10, min_font_size=30)
pyplot.figure(2)
wordcloud.fit_words(freq)
pyplot.imshow(wordcloud)
pyplot.axis('off')
pyplot.show()