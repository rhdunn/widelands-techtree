all: svgz png

dot:
	python generate_techtree.py ${DIR}/tribes/barbarians > barbarians.dot
	python generate_techtree.py ${DIR}/tribes/empire > imperials.dot
	python generate_techtree.py ${DIR}/tribes/atlanteans > atlanteans.dot

svgz:
	dot -Tsvg barbarians.dot | gzip -c > barbarians.svgz
	dot -Tsvg imperials.dot | gzip -c > imperials.svgz
	dot -Tsvg atlanteans.dot | gzip -c > atlanteans.svgz

png:
	dot -Tpng barbarians.dot -o barbarians.png
	dot -Tpng imperials.dot -o imperials.png
	dot -Tpng atlanteans.dot -o atlanteans.png

clean:
	rm -f *.svgz
	rm -f *.png

