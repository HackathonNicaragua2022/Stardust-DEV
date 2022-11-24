function actualizar_hatos(itemID) {
  let selectItem = document.getElementById(itemID);
  selectItem.innerHTML = "<option value=''>Seleccionar Hato</option>";

  let ajax = new XMLHttpRequest();
  ajax.open("GET", "get_hatos");
  ajax.send();

  ajax.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        let respuesta = JSON.parse(this.responseText);

        for (let i = 0; i < respuesta.length; i++) {
          let temp = document.createElement("option");
          temp.value = respuesta[i].codigo;
          temp.textContent = respuesta[i].codigo;
          selectItem.appendChild(temp);
        }
  }}}}

function actualizar_razas(itemID){
  let selectItem = document.getElementById(itemID);
  selectItem.innerHTML = "<option value=''>Seleccionar Raza</option>";

  let ajax = new XMLHttpRequest();
  ajax.open("GET", "get_razas");
  ajax.send();

  ajax.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        let respuesta = JSON.parse(this.responseText);
        for (let i = 0; i < respuesta.length; i++) {
          let temp = document.createElement("option");
          temp.value = respuesta[i].nombre;
          temp.textContent = respuesta[i].nombre;
          selectItem.appendChild(temp);
        }}}}
}

function actualizar_bovinos() {

}

function agregar_bovino() {
  let ajax = new XMLHttpRequest();
  ajax.open("GET", "agregarbovino");

  ajax.send();
  ajax.onreadystatechange = function () {
    if (this.readyState == 4) {
      if (this.status == 200) {
        Swal.fire({
          title: '<strong>Agregar un nuevo Bovino</strong>',
          width: 800,
          html: ajax.responseText,
          showCloseButton: true,
          showCancelButton: false,
          focusConfirm: false,
          confirmButtonText:
            'Agregar',
          confirmButtonAriaLabel: 'Agregar',

        })
      }
    }
  };
}


