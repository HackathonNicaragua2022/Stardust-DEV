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

function actualizar_vacunas(itemID){
  let selectItem = document.getElementById(itemID);
  selectItem.innerHTML = "<option value=''>Seleccionar Vacuna</option>";

  let ajax = new XMLHttpRequest();
  ajax.open("GET", "get_vacunas");
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
  let 
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
          showCloseButton: false,
          showCancelButton: false,

        }).then((result) => {
          if (result.isConfirmed) {
            let form
            let data = new FormData(form);

            let ajax = new XMLHttpRequest();
            ajax.open("POST","agregarbovino");

            ajax.send(data);
            ajax.onreadystatechange = function(){
              if(this.readyState == 4){
                if(this.status == 200){
                  Swal.fire(
                    'Exito',
                    this.responseText,
                    'success'
                    );
                }
                else if(this.status == 400){
                  swal.fire(
                    'Error',
                    this.responseText,
                    'error'
                    );
                }
              }
            }

        }})
      }
    
    }
  };
}

function enviar_bovino(form){
  

}


