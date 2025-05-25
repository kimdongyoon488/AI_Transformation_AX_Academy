from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#호텔 리뷰 데이터
# 1: 긍정적인 평가, 0: 부정적인 평가
x = ["The service is great", "The food is not tasty", "The room is neat", "The soundproofing is not good"]
y = [1, 0, 1, 0] 
 

# 벡터화
vectorizer = CountVectorizer()
x_vectorized = vectorizer.fit_transform(x)

# 학습
model = MultinomialNB()
model.fit(x_vectorized, y)

# 예측
new = ["The service is great", "The soundproofing is not good"]
new_vectorized = vectorizer.transform(new)
preds = model.predict(new_vectorized)

print("예측 결과:", preds)
