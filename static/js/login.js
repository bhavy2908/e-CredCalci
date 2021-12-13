function validate() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  if (username == "" && password == "") {
    alert("Credentials required");
    return false;
  }
 else {
    alert("login successful");
  }

//  if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(main.username.value))
//   {
//     alert("You have entered an invalid email address!")
//     return (false);
//   }


    
}


