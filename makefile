make:
	@python3 picmaker.py
	@convert image.ppm image.png

clean:
	rm *.ppm
	rm *.png
