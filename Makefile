all: aiTrans openaiConnector

LANGUAGE=python
FLAGS=-a

boot: src/aiTrans.ai src/openaiConnector.ai
	src/bootTrans.py -s src/aiTrans.ai $(FLAGS) -l $(LANGUAGE) > aiTrans.py
	chmod +x aiTrans.py
	src/bootTrans.py -s src/openaiConnector.ai $(FLAGS) -l $(LANGUAGE) > openaiConnector.py

aiTrans: src/aiTrans.ai
	python ./aiTrans.py -s src/aiTrans.ai $(FLAGS) -l $(LANGUAGE) > tmp.py
	mv tmp.py aiTrans.py
	chmod +x aiTrans.py

openaiConnector: src/openaiConnector.ai
	python ./aiTrans.py -s src/openaiConnector.ai $(FLAGS) -l $(LANGUAGE) > tmp.py
	mv tmp.py openaiConnector.py

