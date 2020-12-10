$(document).ready(function() {

  var role_usuario = 'estudiante';
  $("#opciones_fincas").hide();
  $('#fincasRecomendacion').hide();
  $('#cultivos').hide();
  $("#adicionarFinca").hide();


  $('#plan_estudio_opcion').click(function() {
    $("#plan_estudio").show();
    $("#opciones_fincas").hide();
    $("#visualizar_mis_cursos").hide();
    $("#materias_visualizar").hide();
    event.preventDefault();
  });

  $('#mis_fincas').click(function() {
    $("#fincasRecomendacion").hide();
    $("#opciones_fincas").show();
    $('#cultivos').hide();
    $("#adicionarFinca").hide();
    event.preventDefault();
  });

  $('#adicionar_finca').click(function() {
    $("#adicionarFinca").show();
    $("#opciones_fincas").hide();
    $('#cultivos').hide();
    event.preventDefault();
  });


  $('#recomendar_cultivos').click(function() {
    $("#opciones_fincas").hide();
    $("#adicionarFinca").hide();
    var documento = $('#documento').text();
    var json_text = '{}'
    const data_json = JSON.parse(json_text)
    data_json["documento"] = documento;
    $.ajax({
      data : data_json,
      type : 'POST',
      url : '/recomendar'
        }).done(function(data) {
      if(data.response == "nofincas"){
        console.log('entre no cursos');
        $("#visualizar_mis_cursos").show();
        var div_general_mis_cursos = $('#visualizar_mis_cursos');
        div_general_mis_cursos.append("<div class='row'><br><h4>Mis fincas</h4><hr/><br></div>");
        div_general_mis_cursos.append("<br><br><h4 class='text-center'>No tiene fincas</h4>")
      }else{
        console.log(data.fincas);
        var dataFincas = data.fincas
        $('#fincasUsuarioRecomendacion').empty();
        $.each(dataFincas, function (index, value) {
              $('#fincasUsuarioRecomendacion').append($('<option/>', {
                  value: value,
                  text : value
              }));
            });
            $('#fincasRecomendacion').show();
          }
      event.preventDefault();
      });
    event.preventDefault();
  });

  $('#registrarFinca').click(function() {
    var finca = $("#finca").val();
    var zona = $("#zona").val();
    var lum = $("#lum").val();
    var top = $("#top").val();
    var altura = $("#altura").val();
    var temp = $("#temp").val();
    var hum = $("#hum").val();
    var ph = $("#ph").val();
    var depto = $("#depto").val();
    var region = $("#region").val();
    var documento = $('#documento').text();
    var json_text = '{}'
    const data_json = JSON.parse(json_text)
    data_json["nombre"] = finca;
    data_json["zona"] = zona;
    data_json["luminosidad"] = lum;
    data_json["topografia"] = top;
    data_json["altura"] = altura;
    data_json["temperatura"] = temp;
    data_json["humedad"] = hum;
    data_json["ph"] = ph;
    data_json["departamento"] = depto;
    data_json["region"] = region;
    data_json["documento"] = documento;
    console.log(data_json)
    $.ajax({
      data : data_json,
      type : 'POST',
      url : '/registrarFinca'
        }).done(function(data) {
      if(data.response == "Error"){
         swal({
                 title: "Oops!",
                 text: "No se pudo registrar la finca",
                 icon: "error"
               });

      }else{
        swal({
         title: "Oops!",
         text: "Registro exitoso",
         icon: "success"
        });
      }
      event.preventDefault();
   });
   event.preventDefault();
   });


  $('#obtenerRecomendacion').click(function() {
  $('#cultivos').empty();
    var finca = $('#fincasUsuarioRecomendacion').val();
    var documento = $('#documento').text();
    console.log(finca)
    console.log(documento)
    var json_text = '{}'
    const data_json = JSON.parse(json_text)
    data_json["documento"] = documento;
    data_json["finca"] = finca;
    $.ajax({
      data : data_json,
      type : 'POST',
      url : '/recomendarcultivo'
        }).done(function(data) {
      if(data.response == "Error"){
         swal({
                 title: "Oops!",
                 text: data.mensaje,
                 icon: "error"
               });

      }else{
        console.log(data.cultivos);
        var cultivos = data.cultivos;
        var lencultivo = cultivos.length;
        var div_general_mis_cursos = $('#cultivos');
        $('#cultivos').show()
        div_general_mis_cursos.append("<br><div class'row'><br><br><h4>Cultivos Recomendados</h4><hr/><br><br></div>");
        div_general_mis_cursos.append("<br><div class='row' id='cultivoNombres'></div>")
        for(var i = 0; i < lencultivo; i++){
            $('#cultivoNombres').append("<br><div class='col'><h3>"+cultivos[i]+"</h3><br><img src='../static/images/"+cultivos[i]+".png' alt="+cultivos[i]+" width='200' height='200'></div>")
        }
          }
      event.preventDefault();
      });
  });


  $('#ver_fincas').click(function() {
    var documento = $('#documento').text();
    var json_text = '{}'
    const data_json = JSON.parse(json_text)
    data_json["documento"] = documento;
    $.ajax({
      data : data_json,
      type : 'POST',
      url : '/misfincas'
    }).done(function(data) {
      if(data.response == "nofincas"){
        console.log('entre no cursos');
        $("#visualizar_mis_cursos").show();
        var div_general_mis_cursos = $('#visualizar_mis_cursos');
        div_general_mis_cursos.append("<div class'row'><br><h4>Mis cursos</h4><hr/><br></div>");
        div_general_mis_cursos.append("<br><br><h4 class='text-center'>No tiene fincas</h4>")
      }else{
        console.log(data.fincas);
      }
      event.preventDefault();
      });
    event.preventDefault();
  });


  $('#btn_logout').click(function() {
    window.location = '/'
    event.preventDefault();
  });

});
