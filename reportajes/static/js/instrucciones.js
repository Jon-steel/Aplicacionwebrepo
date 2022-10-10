$(document).ready(function () {
 
// actualizacion de reporteros
  $(document).on('click', '#actualizar', function () {
      var id_reportero = $(this).val();
      var nombre = $('#nombre' + id_reportero).text();
      var telefono = $('#telefono'+ id_reportero).text();
      var correo = $('#correo' + id_reportero).text();

      console.log(id_reportero);
      console.log(nombre);
      $('#actualizar_report').modal('show');
      $('#id_reportero_a').val(id_reportero);
      $('#r_nombre_a').val(nombre);
      $('#r_telefono_a').val(telefono);
      $('#r_correo_a').val(correo);

  });
// eliminacion de reporteros
  $(document).on('click', '#eliminar', function () {
    var id_reportero = $(this).val();
    var nombre = $('#nombre' + id_reportero).text();
    
    $('#eliminar_report').modal('show');
    $('#id_reportero_e').val(id_reportero);
    $('#r_nombre_e').val(nombre);

});

// actualizacion de camarografos
$(document).on('click', '#actualizarca', function () {
  var id_camarografo = $(this).val();
  var nombre = $('#nombre' + id_camarografo).text();
  var telefono = $('#telefono'+ id_camarografo).text();
  var correo = $('#correo' + id_camarografo).text();

  console.log(id_camarografo);
  console.log(nombre);
  $('#actualizar_camarografo').modal('show');
  $('#id_camarografo_a').val(id_camarografo);
  $('#c_nombre_a').val(nombre);
  $('#c_telefono_a').val(telefono);
  $('#c_correo_a').val(correo);

});

// eliminacion de camarografos
$(document).on('click', '#eliminarca', function () {
  var id_camarografo = $(this).val();
  var nombre = $('#nombre' + id_camarografo).text();
  
  $('#eliminar_camarografo').modal('show');
  $('#id_camarografo_e').val(id_camarografo);
  $('#c_nombre_e').val(nombre);

});


  $(document).ready(function () {
      table =  $('#tabla_reportajes').DataTable({
        "language":{
            "lengthMenu":" Orden de Datos _MENU_  ",
            "zeroRecords": "Lo sentimos. No se encontraron registros que coincidan. <p align='center'><br/><h5 class='carga'>Pruebe con otra opción...</h5></p>",
                  "info": "PÁGINA _PAGE_ DE _PAGES_",
                  "infoEmpty": "No hay registros aún.",
                  "infoFiltered": "(Mostrando _TOTAL_  de un total de _MAX_ registros)",
                  "search" : "Buscar:",
                  "LoadingRecords": "Cargando ...",
                  "Processing": "Procesando...",
                  "SearchPlaceholder": "Comience a teclear...",
                  " scrollX": "true",
                  "paginate": {
          "previous": "<i class='fas fa-arrow-alt-circle-left'></i>",
          "next": "<i class='fas fa-arrow-alt-circle-right'></i>",
          }
          }
        });
      
    }); 

    $(document).ready(function () {
      table =  $('#tabla_reporteros').DataTable({
        "language":{
            "lengthMenu":" Orden de Datos _MENU_  ",
            "zeroRecords": "Lo sentimos. No se encontraron registros que coincidan. <p align='center'><br/><h5 class='carga'>Pruebe con otra opción...</h5></p>",
                  "info": "PÁGINA _PAGE_ DE _PAGES_",
                  "infoEmpty": "No hay registros aún.",
                  "infoFiltered": "(Mostrando _TOTAL_  de un total de _MAX_ registros)",
                  "search" : "Buscar:",
                  "LoadingRecords": "Cargando ...",
                  "Processing": "Procesando...",
                  "SearchPlaceholder": "Comience a teclear...",
                  " scrollX": "true",
                  "paginate": {
          "previous": "<i class='fas fa-arrow-alt-circle-left'></i>",
          "next": "<i class='fas fa-arrow-alt-circle-right'></i>",
          }
          }
        });
      
    }); 

    $(document).ready(function () {
      table =  $('#tabla_camarografos').DataTable({
        "language":{
            "lengthMenu":" Orden de Datos _MENU_  ",
            "zeroRecords": "Lo sentimos. No se encontraron registros que coincidan. <p align='center'><br/><h5 class='carga'>Pruebe con otra opción...</h5></p>",
                  "info": "PÁGINA _PAGE_ DE _PAGES_",
                  "infoEmpty": "No hay registros aún.",
                  "infoFiltered": "(Mostrando _TOTAL_  de un total de _MAX_ registros)",
                  "search" : "Buscar:",
                  "LoadingRecords": "Cargando ...",
                  "Processing": "Procesando...",
                  "SearchPlaceholder": "Comience a teclear...",
                  " scrollX": "true",
                  "paginate": {
          "previous": "<i class='fas fa-arrow-alt-circle-left'></i>",
          "next": "<i class='fas fa-arrow-alt-circle-right'></i>",
          }
          }
        });
      
    });
 });