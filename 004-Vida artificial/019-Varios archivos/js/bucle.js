function bucle(){
    contexto.fillStyle = "rgba(255,255,255,0.1)"
    contexto.fillRect(0,0,anchura,altura)
    for(let i = 0;i<comidas.length;i++){
        comidas[i].dibuja(contexto);
    }
    // Para cada una de las personas
    for(let i = 0;i<personas.length;i++){
        // Mueve a la persona
        personas[i].mueve();
        // Dibuja a la persona
        personas[i].dibuja(contexto);
        // constantemente miramos que comida tenemos mas cerca
        if(personas[i].getEnergia() < 10){
            personas[i].buscaComida(comidas);
        }
        // Matamos a la persona?
        if(personas[i].getEnergia() < 0){
            personas.splice(i,1)
        }
    } 

    clearTimeout(temporizador)
    temporizador = setTimeout("bucle()",100)
}