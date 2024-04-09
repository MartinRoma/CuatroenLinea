let doc = "";
let seguir = prompt("Ingrese si para iniciar Boocle");
while(seguir == "si"){
  doc=prompt("Es Doctor?");
  switch (doc) {
    case "si":
      alert("Hola Doc");
      break;
    case "no":
      alert("Hola");
      break;
    default:
      alert("No entendi");
      break;
  }
  seguir=prompt("Desea seguir?");
}
