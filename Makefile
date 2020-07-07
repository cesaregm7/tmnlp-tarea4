bigram ?= True
frase ?= We staying in the hotel for my sister\'s wedding. The coctel was on the rooftop with a impressionant view. The staff was the most awesome of this place, wherever you need they had a solution!!! Breakfast was delicious and the room was really beautiful.
train:
	python -c "from src.models.train import train; train($(bigram))"
visualization:
	python -c "from src.models.train import train; from src.visualization.visualize import generate_visualization; dw,lda_model,corpus,id2word = train($(bigram)); generate_visualization(lda_model,corpus,id2word)"
predict:
	python -c "from src.models.predict import predict; print(predict(sentence='$(frase)',bigrams=$(bigram)))"