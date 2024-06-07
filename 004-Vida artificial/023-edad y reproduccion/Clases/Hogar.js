class Hogar extends Entidad{
    constructor(){
        super()
    }
    dibuja(contexto){
        contexto.fillStyle = "blue"
        contexto.beginPath()     
        contexto.arc(this.x,this.y,2,0,Math.PI*2)
        contexto.fill()
    }
}