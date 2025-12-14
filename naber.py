let email = document.getElementById("email");
let password = document.getElementById("password");

let emailPlaceholder = document.getElementById("emailPlaceholder");

let showOrHide = document.getElementById("showOrHide");

let login = document.getElementById("login");

let fadingImages = document.querySelectorAll(".fadingImages");

let frame1 = document.getElementById("frame1");


function displayImages(from, to) {

  let current = to;

 setInterval(function() {

    fadingImages[current].style.opacity='0';
    console.log(fadingImages[current])


    if (current == from) { 
        current= to+1;
    }
    current--;
    fadingImages[current].style.opacity='1';

  }, 4000);

}
displayImages(0, 3);


function check(){

    console.log("hello");
    if(email.value == ""){
        emailPlaceholder.style.fontSize = "12px";
        emailPlaceholder.style.top = "8px";
        emailPlaceholder.style.opacity= "0.7"
        email.style.paddingTop="";


    
    } else{
        emailPlaceholder.style.fontSize = "10px";
        emailPlaceholder.style.top = "3px";
        emailPlaceholder.style.opacity= "0.7"
        email.style.fontSize = "12px"
        email.style.paddingTop="20px";

        
    }

    if(password.value==""){

        showOrHide.innerText = "";
        passwordPlaceholder.style.fontSize = "12px";
        passwordPlaceholder.style.top = "8px";
        passwordPlaceholder.style.opacity= "0.7"
        password.style.paddingTop="";

    } else{
        passwordPlaceholder.style.fontSize = "10px";
        passwordPlaceholder.style.top = "3px";
        passwordPlaceholder.style.opacity= "0.7"
        password.style.fontSize = "12px"
        password.style.paddingTop="20px";

        showOrHide.innerHTML = "Show";

    }

    
    if(email.value !="" && password.value != "" && password.value.length >=6){
        login.style.backgroundColor = "#049bff";
        login.style.cursor="pointer";
    } else{
        login.style.backgroundColor = "";
        login.style.cursor="";

    }



}

function showOrHide1(){

    if(showOrHide.innerHTML =="Show"){
        showOrHide.innerHTML="Hide";

        password.type="text"; 
        
    } else{
        showOrHide.innerHTML = "Show";
        password.type="password"; 
    }

}
