

Resultados_hw5.pdf : Resultados_HW5.tex *.png
	pdflatex Resultados_HW5.tex	
*.png: plots_canal_ionico.py  CircuitoRC.py *.dat
	python plots_canal_ionico.py 
	python CircuitoRC.py
datos.dat: a.out 
	./a.out > archivos_salida0.dat archivos_salida1.dat
a.out: canal_icono.c
	gcc canal_icono.c -lm
