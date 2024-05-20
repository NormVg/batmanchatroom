
function typeWriter(id){
  var i = 0;
  var txt = document.getElementById(id).innerText
  var speed = 10; 
  document.getElementById(id).innerHTML = ""
  function typeWriter_inn() {
  
    
    if (i < txt.length) {
      
      document.getElementById(id).innerHTML += txt.charAt(i);
      i++;
      setTimeout(typeWriter_inn, speed);
    }
  }
  typeWriter_inn()
  }
  // typeWriter("head-wel")
  // typeWriter("head-eve")