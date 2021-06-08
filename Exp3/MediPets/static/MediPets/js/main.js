document.addEventListener('DOMContentLoaded', () => {
	const imgLightBox = document.querySelectorAll('.materialboxed');
	M.Materialbox.init(imgLightBox, {
		inDuration: 1000,
		outDuration: 1000
	});
});


/*let hamburguesa = document.getElementById('hamburguesa');

hamburguesa.addEventListener('click', () => {	
	hamburguesa.classList.toggle('animacion');
});*/

document.getElementById("btnRegistrarse").addEventListener("click", register);
document.getElementById("btnIniciarSesion").addEventListener("click", IniciarSesion);
window.addEventListener("resize", anchoPagina);
//Variables
var contenedor_LoginRegister = document.querySelector(".Contenedor-Login-Register")
var formulario_Login = document.querySelector(".Formulario-Login")
var formulario_register = document.querySelector(".formulario-Register")
var caja_traseraLogin = document.querySelector(".cajaTraseraLogin")
var caja_traseraRegister = document.querySelector(".cajaTraseraRegistro")

function anchoPagina(){	
	if(window.innerWidth > 850){	
		caja_traseraLogin.style.display = "block";
		caja_traseraRegister.style.display = "block";
	}else{	
		caja_traseraRegister.style.display = "block";
		caja_traseraRegister.style.opacity = "1";
		caja_traseraLogin.style.display = "none";
		formulario_Login.style.display = "block";
		formulario_register.style.display = "none";
		contenedor_LoginRegister.style.left = "0px";
	}
}
anchoPagina();

function register(){
	if(window.innerWidth > 850){	
	formulario_register.style.display = "block";
	contenedor_LoginRegister.style.left = "410px";
	formulario_Login.style.display = "none";
	caja_traseraRegister.style.opacity = "0";
	caja_traseraLogin.style.opacity = "1";
}	else{
		formulario_register.style.display = "block";
		contenedor_LoginRegister.style.left = "0px";
		formulario_Login.style.display = "none";
		caja_traseraRegister.style.display = "none";
		caja_traseraLogin.style.display = "block";
		caja_traseraLogin.style.opacity = "1";
	}
}
function IniciarSesion(){	
	if(window.innerWidth > 850){
		formulario_register.style.display = "none";
		contenedor_LoginRegister.style.left = "10px";
		formulario_Login.style.display = "block";
		caja_traseraRegister.style.opacity = "1";
		caja_traseraLogin.style.opacity = "0";
	}else{	
		formulario_register.style.display = "none";
		contenedor_LoginRegister.style.left = "0px";
		formulario_Login.style.display = "block";
		caja_traseraRegister.style.display = "block";
		caja_traseraLogin.style.display = "none";	
	}
}


$(document).ready(function()
        {
            $("#solicitar").click(function(){

                $.get("https://mindicador.cl/api",
                    function(data){
                        
                        $.each(data,function(i,item){
                            $("#monedas").append("<tr><td>"+item.codigo+"</td><td>"+item.nombre +
                            "</td><td>"+'$' +item.valor+ "</td><td>");
                            

                        });

                    });
            });
        })