$(document).ready(function() {
  var role_usuario = 'agricultor';
  $("#enlace_agricultor").hide()

  $('#coordinator_account_form').click(function() {
    role_usuario = 'administrador'
    $("#role_login").text("Administrador")
    $("#enlace_agricultor").show()
    $("#enlace_administrador").hide();
    event.preventDefault();
  });

  $('#student_account_form').click(function() {
    role_usuario = 'agricultor'
    $("#role_login").text("Agricultor")
    $("#enlace_agricultor").hide()
    $("#enlace_administrador").show();
    event.preventDefault();
  });

  $('#btn_login').click(function(){
      if(role_usuario == 'agricultor')
      {
        var codigo = $("#codigo_login").val();
        var password = $("#password_login").val();
        if(password == ''){
          swal({
                 title: "Oops!",
                 text: "Ingresa contraseña",
                 icon: "error"
               });
        }else if(codigo == ''){
          swal({
                 title: "Oops!",
                 text: "Ingresa documento",
                 icon: "error"
               });
        }else{
            var json_text = '{}'
            const data_json = JSON.parse(json_text)
            data_json["documento"] = codigo;
            data_json["password"] = password;
            console.log(data_json);
            $.ajax({
            data : data_json,
            type : 'POST',
            url : '/loginagricultor'
          })
          .done(function(data) {
            if(data.response == "Error"){
              swal({
                     title: "Oops!",
                     text: "Credenciales inválidas",
                     icon: "error"
                   });
            }
            else{
                   console.log(data.documento)
                   swal("It`s Okey", data.response,"success");
                   var json_text = '{}'
                   const data_json = JSON.parse(json_text)
                   data_json["documento"] = data.documento;
                   data_json["nombre"] = data.nombre;
                   console.log(data_json)
                   $.ajax({
                   data : data_json,
                   type : 'POST',
                   url : '/agricultor',
                   success: function(response){
                        //console.log(response);
                  var x = window.open("","_self");
                  x.document.open();
                  x.document.write(response);
                  x.document.close();

                    },
                    error: function(error){
                        console.log(error);
                    }
                 });
            }

        });
        }
      }
      else
      {
        var codigo = $("#codigo_login").val();
        var password = $("#password_login").val();
        if(password == ''){
          swal({
                 title: "Oops!",
                 text: "Ingresa contraseña",
                 icon: "error"
               });
        }else if(codigo == ''){
          swal({
                 title: "Oops!",
                 text: "Ingresa documento",
                 icon: "error"
               });
        }else{
            var json_text = '{}'
            const data_json = JSON.parse(json_text)
            data_json["documento"] = codigo;
            data_json["password"] = password;
            console.log(data_json);
            $.ajax({
            data : data_json,
            type : 'POST',
            url : '/loginadmin'
          })
          .done(function(data) {
            if(data.response == "Error"){
              swal({
                     title: "Oops!",
                     text: "Credenciales inválidas",
                     icon: "error"
                   });
            }
            else{
                   console.log(data.documento)
                   swal("It`s Okey", data.response,"success");
                   var json_text = '{}'
                   const data_json = JSON.parse(json_text)
                   data_json["documento"] = data.documento;
                   data_json["nombre"] = data.nombre;
                   console.log(data_json)
                   $.ajax({
                   data : data_json,
                   type : 'POST',
                   url : '/administrador',
                   success: function(response){
                        //console.log(response);
                  var x = window.open("","_self");
                  x.document.open();
                  x.document.write(response);
                  x.document.close();

                    },
                    error: function(error){
                        console.log(error);
                    }
                 });
            }

        });
        }
      }

    event.preventDefault();
  });





});
