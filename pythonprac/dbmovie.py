from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.rvhpcnz.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 가버나움 평점 찍기
movie = db.movies.find_one({'title':'가버나움'})
print(movie['star'])

# 가버나움과 같은 평점의 영화 가져오기
temp_star = movie['star']
temp_movies = list(db.movies.find({'star':temp_star}))
for movie in temp_movies:
    print(movie['title'])

# 가버나움의 영화 평점을 0점으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})