class Comida extends Entidad{
    constructor(){
        super()
    }
    dibuja(contexto){
        contexto.fillStyle = "red"
        contexto.beginPath()     
        contexto.arc(this.x,this.y,2,0,Math.PI*2)
        contexto.fill()
    }
}