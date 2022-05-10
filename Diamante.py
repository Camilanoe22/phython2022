# Dibuja un fondo
Rect(0, 0, 400, 400, relleno=gradiente('azulPolvo', 'cianClaro', inicio='superior'))

# Cree la forma externa del diamante usando un Polígono.
### Ponga su código aquí ###
Poligono(60,150,200,300,340,150,300,100,100,100, relleno=gradiente('blanco','azulclaro',inicio='centro'),borde='negro',anchuraDeBorde=4)
# Cree la parte interna más brillante del diamante usando un Polígono.
### Ponga su código aquí ###
Poligono(125,150,200,300,275,150,200,100,relleno='azur',borde='negro')
# Cree las líneas de corte.
### Ponga su código aquí ###
Linea(100,100,125,150,relleno='negro',anchuraDeLinea=2)
Linea(60,150,340,150,relleno='negro',anchuraDeLinea=2)
Linea(300,100,275,150,relleno='negro',anchuraDeLinea=2)
# ¡Termine agregando un brillo al diamante!
### Ponga su código aquí ##
Estrella(265,120,15,6,relleno='blanco',redondez=15)
