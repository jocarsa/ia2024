class Persona extends Entidad{
    constructor(){
        super()
        this.a = Math.random()*Math.PI*2
        this.r = Math.round(Math.random()*255)
        this.g = Math.round(Math.random()*255)
        this.b = Math.round(Math.random()*255)
        this.e = Math.random()*100
        this.d = (Math.random()-0.5)/10
    }
    mueve(){
        if(this.e > 10){
            this.d += (Math.random()-0.5)/40
            this.a += this.d
        }

        this.x += Math.cos(this.a)
        this.y += Math.sin(this.a)
        this.e -= 0.1
        this.rebotePared()
    }
    getEnergia(){
        return this.e;
    }
    dibuja(contexto){
        contexto.fillStyle = "rgb("+this.r+","+this.g+","+this.b+")"
        contexto.fillRect(this.x,this.y,2,2)
    }
    buscaComida(comidas){
        let mejorcandidato = 0
        let mejordistancia = 1000000
        for(let i = 0;i<comidas.length;i++){
            let distancia = calculaDistancia(this.x,this.y,comidas[i].x,comidas[i].y)
            if(distancia < mejordistancia){
                mejorcandidato = i;
                mejordistancia = distancia
            }
        }
        /*contexto.beginPath()
        contexto.moveTo(this.x,this.y)
        contexto.lineTo(comidas[mejorcandidato].x,comidas[mejorcandidato].y)
        contexto.stroke()*/
        this.a = anguloEntreDosPuntos(
            this.x, 
            this.y, 
            comidas[mejorcandidato].x, 
            comidas[mejorcandidato].y
        ) 
        if(calculaDistancia(
            this.x,
            this.y,
            comidas[mejorcandidato].x,
            comidas[mejorcandidato].y
        ) < 10){
            console.log("como")
            this.come()
        }
    }
    come(){
        this.e = 100
    }
    rebotePared(){
        if(this.y < 0 || this.y > altura){
            this.a = calculoRebotePared(this.a , "horizontal")
        }
        if(this.x < 0 || this.x > anchura){
            this.a = calculoRebotePared(this.a , "vertical")
        }
    }
}