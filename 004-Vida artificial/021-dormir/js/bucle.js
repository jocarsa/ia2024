function bucle(){
    contexto.fillStyle = "rgba(255,255,255,0.1)"
    contexto.fillRect(0,0,anchura,altura)
    for(let i = 0;i<comidas.length;i++){
        comidas[i].dibuja(contexto);
    }
    for(let i = 0;i<hogares.length;i++){
        hogares[i].dibuja(contexto);
    }
    // Para cada una de las personas
    for(let i = 0;i<personas.length;i++){
        // Mueve a la persona
        personas[i].vive();
        if(personas[i].getEnergia() < 0){
            personas.splice(i,1)
        }
    } 
    console.log(personas.length)
    clearTimeout(temporizador)
    temporizador = setTimeout("bucle()",0)
}