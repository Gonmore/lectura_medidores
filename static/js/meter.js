function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  } 

$(document).ready(function(){
    let tablaj = $('#tabla_medidores').DataTable({
        scrollY:      300,
        paging:       true,
        deferRender:  false,
        pageLength :  25,
        responsive: true,
        scroller:     true,
        autofill: true,
        dom: 'QBlfrtip',
        buttons: [
          'csvHtml5', 'excelHtml5', 'pdfHtml5', 'print','colvis'
        
        ],
        language: {
          url: 'https://cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json',
        },
        orderCellsTop: true,
        columnDefs: [
          { responsivePriority: 1, targets: -1 }  // Última columna siempre visible
      ]
      }
      );
      $('input:checkbox').on('change', function () {
        tablaj.draw();
    });
    $('.btn_ver').on('click',async function(){
      var name = $(this).data('name');
      await $.ajax({
        url: '/ajax_ver_med',
        type: 'post',
        cache:false,
        data: {meter:name},
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function(data){ 
          $('.modal-body').html(data); 
          $('.modal-body').append(data.htmlresponse);
          $('.modal-title').append('Historial: '+name);
          $('.modal-footer').append('<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Cerrar</button>');
          $('#favModal').modal('show');
          let tablav = $('#tabla_historial').DataTable({
            scrollY:      300,
            paging:       true,
            deferRender:  false,
            pageLength :  25,
            responsive: true,
            scroller:     true,
            autofill: true,
            dom: 'QBlfrtip',
            buttons: [
              'csvHtml5', 'excelHtml5', 'pdfHtml5', 'print','colvis'
            
            ],
            language: {
              url: 'https://cdn.datatables.net/plug-ins/1.10.24/i18n/Spanish.json',
            },
            orderCellsTop: true,
            columnDefs: [
              { responsivePriority: 1, targets: -1 }  // Última columna siempre visible
          ]
          }
          )}
      })
    })
    $('#favModal').on('hidden.bs.modal', function(){
      $('#favModal .modal-footer').empty();
      $('#favModal .modal-title').empty();
      $('#favModal .modal-body').empty();
    }) 
    $('.btn_leer').on('click',async function(){
      var name = $(this).data('name');
      await $.ajax({
        url: '/ajax_lectura_simple',
        type: 'post',
        cache:false,
        data: {meter:name},
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function(data){ 
          $('.modal-body').html(data); 
          $('.modal-body').append(data.htmlresponse);
          $('.modal-title').append('Lectura instantanea');
          $('.modal-footer').append('<button type="button" class="btn btn-primary" data-bs-dismiss="modal">Confirmar</button>');
          $('#favModal').modal('show'); 
      }
      })
    })

    $('.btn_editar').on('click',async function(){
      var name = $(this).data('name');
      await $.ajax({
        url: '/editar/'+ name,
        type: 'get',
        cache:false,
        data: {name:name},
        success: function(data){ 
          $('.modal-body').html(data); 
          $('.modal-body').append(data.htmlresponse);
          $('.modal-title').append('Editar medidor ');
          $('#favModal').modal('show'); 
      }
      })
      $('#form_editado').submit(function(event) {
        console.log('entro submit');
        event.preventDefault();
        $.ajax({
            url: '/editar/'+ name,
            type: 'POST',
            data: $(this).serialize(),
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            success: function(response) {
                if (response.success) {
                    $('#favModal').modal('hide');
                    location.reload();
                } else {
                    // Mostrar errores en el formulario
                    for (var field in response.errors) {
                        $('#id_' + field).after('<div class="error">' + response.errors[field] + '</div>');
                    }
                }
            }
        });
    });
    })

    $('.btn_nuevo').on('click',async function(){
      await $.ajax({
        url: '/nuevo/',
        type: 'get',
        cache:false,
        success: function(data){ 
          $('.modal-body').html(data); 
          $('.modal-body').append(data.htmlresponse);
          $('.modal-title').append('Agregar medidor');
          $('#favModal').modal('show'); 
      }
      })
      $('#form_new').submit(function(event) {
        console.log('entro submit');
        event.preventDefault();
        $.ajax({
            url: '/nuevo/',
            type: 'POST',
            data: $(this).serialize(),
            headers: {
              "X-Requested-With": "XMLHttpRequest",
              "X-CSRFToken": getCookie("csrftoken"),
            },
            success: function(response) {
                if (response.success) {
                    $('#favModal').modal('hide');
                    location.reload();
                } else {
                    // Mostrar errores en el formulario
                    for (var field in response.errors) {
                        $('#id_' + field).after('<div class="error">' + response.errors[field] + '</div>');
                    }
                }
            }
        });
    });
    })
    
    

    $('.btn_quitar').on('click',async function(){
      var name = $(this).data('name');
      $('.modal-body').append('Esta seguro de eliminar este medidor?');
      $('.modal-title').append('Eliminar medidor');
      $('.modal-footer').append('<button type="button" class="btn btn-primary eliminar" data-name="'+name+'">Confirmar</button><button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>');    
      $('#favModal').modal('show');
      $('.eliminar').on('click',async function(){
      await $.ajax({
        url: '/ajax_quitar_med',
        type: 'post',
        cache:false,
        data: {meter_name:name},
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        success: function(data){ 
          $('#favModal').modal('hide');
                    location.reload();
          
      }
      })
    })
  })

})