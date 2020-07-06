train:
	python -c "from src.models.train import train; train($(bigram))"
visualization:
	python -c "from src.models.train import train; from src.visualization.visualize import generate_visualization; dw,lda_model,corpus,id2word = train($(bigram)); generate_visualization(lda_model,corpus,id2word)"
predict:
	python -c "from src.models.predict import predict; print(predict('$(frase)'))"