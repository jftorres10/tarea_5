

Resultados_hw5.pdf : Resultados_hw5.tex *.png
	pdflatex Resultados_hw5.tex
*.png: CircuitoRC.py *.dat
	python CircuitoRC.py
*.png: plots_canal_ionico.py *.dat
	python plots_canal_ionico.py
datos.dat: a.out 
	./a.out > datos.dat
a.out: canal_icono.c
	gcc canal_icono.c
