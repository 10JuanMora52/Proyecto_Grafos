// Definición de conjuntos
{int} Materias = ...;  // Materias numeradas del 1 al 40
{int} Semestres =...; // Semestres (ajustar según el número real)

// Parámetros
int c[Materias][Semestres] = ...; // Costo de cursar cada materia en cada semestre
int prereq[Materias][Materias] = ...; // Matriz binaria de prerrequisitos: 1 si i es prerequisito de j
int val[Materias]= ...;//lista de creditos de la materia

// Variables de decisión
dvar boolean X[Materias][Semestres]; // 1 si materia m se cursa en el semestre s
dvar boolean Y[Materias][Semestres];

//Variables auxliares
dvar float costo_total;
dvar float creditos_semestre[Semestres];

// Función objetivo
minimize sum(m in Materias, s in Semestres) c[m][s] * X[m][s] + sum(m in Materias, s in Semestres)80000*Y[m][s]; // Minimizar el costo total

// Restricciones
subject to {
    // Restricción 1: Cada materia debe cursarse exactamente una vez
    forall(m in Materias)
        sum(s in Semestres) X[m][s] == 1;
        
    //Restriccion de creditos por semestre
    forall(j in Semestres)
      sum (i in Materias)val[i]*X[i][j]<=22;
      
    // Cada semestre minimo una materia    
    forall(j in Semestres)
      sum(i in Materias) X[i][j] >= 1;
    
    //Cambiar de estado
    forall (i in Materias, j in Semestres)
      Y[i][j]>=X[i][j];
    
    //mantener el cambio de estado
    forall(i in Materias, j in Semestres: j >= 2)
      Y[i][j]>=Y[i][j-1];
      
    //prerrequisitos
    forall(i,k in Materias,j in Semestres: j >= 2 && prereq[k][i] == 1)
      X[i][j] <= Y[k][j-1];
    
    //creditos para ver seminario
    sum(i in Semestres: i <=5)X[38][i] == 0;
    
    //obligatorias primero
    sum(i in Materias:i <= 7)X[i][1] == 7;
    
    //solo 7 en primero
    sum(i in Materias)X[i][1] == 7;
      
    // Variable auxiliar de compras
    costo_total == sum(m in Materias, s in Semestres) c[m][s] * X[m][s];
    
    forall(j in Semestres) creditos_semestre[j] == sum (i in Materias)val[i]*X[i][j];
    
  }
