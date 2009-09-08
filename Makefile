all: svgz png

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

