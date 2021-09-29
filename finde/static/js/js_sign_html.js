//checkbox variables
var x = document.getElementById("");
var y = document.getElementById("");

//password correct input variables
var myInput = document.getElementById("psw_1");
var letter = document.getElementById("letter");
var capital = document.getElementById("capital");
var number = document.getElementById("number");
var length = document.getElementById("length");

//checkbox function
function checkToggle() {
    if (x.type && y.type === "password") {
        x.type = "text";
        y.type = "text";
    } else {
        x.type = "password";
        y.type = "password";
    }
    console.log("di")
}

//matching passwords function
function checkPassword(form) {
    x = form.password1.value;
    y = form.password2.value;

    if (x === '')
        alert ("Por favor ingrese contrasena");

    else if (y === '')
        alert ("Por favor confirme contrasena");

    else if (x !== y) {
        alert ("\nLa contrasena no es la misma, intente de nuevo")
        return false;
    }
    else{
        return true;
    }
}

// When the user clicks outside of the password field, hide the message box
    document.getElementById("message").style.display = "none";

// When the user clicks on the password field, show the message box
myInput.onfocus = function() {
    document.getElementById("message").style.display = "block";
}

// Values validation function
myInput.onkeyup = function() {

    var lowerCaseLetters = /[a-z]/g;
    if(myInput.value.match(lowerCaseLetters)) {
        letter.classList.remove("invalid");
        letter.classList.add("valid");
    } else {
        letter.classList.remove("valid");
        letter.classList.add("invalid");
    }

    var upperCaseLetters = /[A-Z]/g;
    if(myInput.value.match(upperCaseLetters)) {
        capital.classList.remove("invalid");
        capital.classList.add("valid");
    } else {
        capital.classList.remove("valid");
        capital.classList.add("invalid");
    }

    var numbers = /[0-9]/g;
    if(myInput.value.match(numbers)) {
        number.classList.remove("invalid");
        number.classList.add("valid");
    } else {
        number.classList.remove("valid");
        number.classList.add("invalid");
    }

    if(myInput.value.length >= 8) {
        length.classList.remove("invalid");
        length.classList.add("valid");
    } else {
        length.classList.remove("valid");
        length.classList.add("invalid");
    }
}


