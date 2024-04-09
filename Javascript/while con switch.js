let c = 1;
let entrada=prompt("Ingrese Altura del numero "+ c);
while(entrada != "ESC"){
  switch (true) { /* el switch true funciona en lugar de poner la base para condiciones en el switch lo cambia a que sea true la condicion en cada case,
    pasando el condicional a los case completamente */
    case entrada <=1.6: // Es 1.6 y no 1,6 no funcionan los decimales con coma
      alert ("Enano");
      break;
    case (entrada <= 1.9)&&(entrada>1.6):
      alert("Medio");
      break;
    case entrada>1.9:
      alert("Alto");
      break;
    default:
      alert("Error");
      break;
  }
  c++;
  entrada=prompt("Ingrese altura del numero "+c);
}
