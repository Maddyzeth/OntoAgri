$(document).ready(function() {

  var role_usuario = 'estudiante';
  $("#adicionarRegla").hide();


  $('#ingresar_regla').click(function() {
    $("#adicionarRegla").show();
    event.preventDefault();
  });

  $('#registrarCultivo').click(function() {
    var cultivo = $("#cultivo").val();
    var tipo = $("#tipo").val();
    var lumMin = $("#lumMin").val();
    var lumMax = $("#lumMax").val();
    var topMin = $("#topMin").val();
    var topMax = $("#topMax").val();
    var alturaMin = $("#alturaMin").val();
    var alturaMax = $("#alturaMax").val();
    var tempMin = $("#tempMin").val();
    var tempMax = $("#tempMax").val();
    var humMin = $("#humMin").val();
    var humMax = $("#humMax").val();
    var phMin = $("#phMin").val();
    var phMax = $("#phMax").val();
    var json_text = '{}'
    const data_json = JSON.parse(json_text)
    data_json["cultivo"] = cultivo;
    data_json["tipo"] = tipo;
    data_json["lumMin"] = lumMin;
    data_json["lumMax"] = lumMax;
    data_json["topMin"] = topMin;
    data_json["topMax"] = topMax
    data_json["alturaMin"] = alturaMin;
    data_json["alturaMax"] = alturaMax;
    data_json["tempMin"] = tempMin;
    data_json["tempMax"] = tempMax;
    data_json["humMin"] = humMin;
    data_json["humMax"] = humMax;
    data_json["phMin"] = phMin;
    data_json["phMax"] = phMax;
    console.log(data_json)
    $.ajax({
      data : data_json,
      type : 'POST',
      url : '/registrarCultivo'
        }).done(function(data) {
      if(data.response == "Error"){
         swal({
                 title: "Oops!",
                 text: "No se pudo registrar el cultivo",
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


  $('#btn_logout').click(function() {
    window.location = '/'
    event.preventDefault();
  });

});
