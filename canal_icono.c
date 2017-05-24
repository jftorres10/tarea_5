#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int condi_frontera(double x, double y , double r, double *xdatos, double *ydatos, int n );
double Num_aleat (double limite );
int main()
{
FILE *in;
int i ;
int n = 42;
double *xdatos = malloc(n*sizeof(double));
double *ydatos = malloc(n*sizeof(double));

in= fopen("Canal_ionico.txt","r");
for ( i = 0; i < n; ++i)
{
	fscanf(in, "%lf %lf\n",&xdatos[i], &ydatos[i]);
	
	/*printf("valores x %f valores y %f\n",xdatos[i], ydatos[i]); lee los datos */
}

double x=5.0;
double y=5.0;
double r= 1.0;
double var= 0.1;

int max_iter = 1000;

double *random_walk_x = malloc(max_iter*sizeof(double));
double *random_walk_y = malloc(max_iter*sizeof(double));
double *random_walk_r = malloc(max_iter*sizeof(double));


random_walk_x[0]=x;
random_walk_y[0]=y;
random_walk_r[0]=r;

int frontera ;
int beta;
frontera = condi_frontera(x,  y ,  r, xdatos,  ydatos,  n);

for (i = 1; i < max_iter; ++i)
{
	x = random_walk_x[i-1]+Num_aleat(var);
	y = random_walk_y[i-1]+Num_aleat(var);
	r = random_walk_r[i-1]+Num_aleat(var);
	if (condi_frontera(x, y , r, xdatos, ydatos,  n ) == 1 )
	{
	 	if (r >= random_walk_r[i-1])
	 	{
	 		/*aceptar los nuevos valores aleatorios para las posciciones x,y,r */
	 		random_walk_x[i] = x;
	 		random_walk_y[i] = y;
	 		random_walk_r[i] = r;
	 	}
	 	else 
	 	{
	 		beta = (double)rand()/RAND_MAX;

	 			if(beta > r/random_walk_r[i-1])
	 			{
	 			/*aceptar los nuevos valores aleatorios para las posciciones x,y,r */
	 				random_walk_x[i] = x;
	 				random_walk_y[i] = y;
	 				random_walk_r[i] = r;
	 			}
	 				else 
	 				{
	 					/*rechazar los nuevos valores aleatorios y quedarse con los anteriores para las posciciones x,y,r */
	 					random_walk_x[i] = random_walk_x[i-1];
	 					random_walk_y[i] = random_walk_y[i-1];
	 					random_walk_r[i] = random_walk_r[i-1];

	 				}
	 	}
	}
	else
	{
		/*rechazar los nuevos valores aleatorios y quedarse con los anteriores para las posciciones x,y,r */
		random_walk_x[i] = random_walk_x[i-1];
	 	random_walk_y[i] = random_walk_y[i-1];
	 	random_walk_r[i] = random_walk_r[i-1];
	}
	printf("%f %f %f\n",random_walk_x[i],random_walk_y[i],random_walk_r[i]);
}

}


int condi_frontera(double x, double y , double r, double *xdatos, double *ydatos, int n )
{
double  r_molecula= 1.0;
/* en respuesta , 1 es no y 0 es si */
 int respuesta = 1 ;
 int i;
 for ( i = 0; i < n; ++i)
 {
 	if( pow(pow(x-xdatos[i],2)+pow(y-ydatos[i],2),0.5) <= r+ r_molecula )
 	{
 		respuesta= 0;
 	}
 }
	return respuesta;

}

double Num_aleat (double limite )
{

double respuesta;
respuesta =limite-(double)rand()/RAND_MAX*2*limite;

return respuesta;
}