var anchura = window.innerWidth;
var altura = window.innerHeight;
document.getElementById("lienzo").width = anchura
document.getElementById("lienzo").height = altura
var contexto = document.getElementById("lienzo").getContext("2d") 
// Creo un conjunto de personas
let personas = []
let comidas = []
var temporizador = setTimeout("bucle()",1000)