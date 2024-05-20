// var lastchat =  "new-client-200";
const searchParams = new URLSearchParams(window.location.search);
var user_name = searchParams.get('user')



function update_chat_room(msg,user,id) {
  
    // console.log(item, index);

    let name_ele = document.createElement("span")
    name_ele.appendChild(document.createTextNode(user))
    
    name_ele.className = "msg-user"
    let msg_ele = document.createElement("div")
    msg_ele.appendChild(document.createTextNode("? "))
    msg_ele.appendChild(name_ele)
    msg_ele.appendChild(document.createTextNode(" > "))
    var msg_span = document.createElement("span")
    msg_span.innerText = msg
    msg_span.id = id
    msg_ele.appendChild(msg_span  )
    msg_ele.className = "msg-box"

    document.getElementById("msgs-box-main").appendChild(msg_ele)
    
    var objDiv = document.getElementById("msgs");
    objDiv.scrollTop = objDiv.scrollHeight
    typeWriter(id)
}







// function message_send(text,user) {
//   console.log(text,user);

//   const apiUrl = "/api/send-msg";

//   const postData = {
//     "user":user,
//     "msg":text
//   };

//   const requestOptions = {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify(postData),
//   };
//   fetch(apiUrl, requestOptions)
//     .then((response) => {
//       if (!response.ok) {
//         throw new Error("Network response was not ok");
//       }
//       return response.json();
//     })
//     .then((data) => {
//       console.log(data);
//     })
//     .catch((error) => {
//       console.error("Error:", error);
//     });
// }

// let chat_form = document.getElementById("msg-form")
// chat_form.addEventListener("submit", (e) => {
//     e.preventDefault();
  
//     let input_Msg = document.getElementById("input-msg");
//     console.log(input_Msg.value)

//     message_send(input_Msg.value, user_name)

//     input_Msg.value = ""
  
    
//   });

// setInterval(update_chat_room, 600);


// For the full code sample see here: https://github.com/ably/quickstart-js
const ably = new Ably.Realtime('XNY10w.VLTrsA:bzpOmfHgzSZYaU8oPn4YQqrEr0RJYT7tYyUKFUTnAyQ');

async function connect_ably(){
  
  await ably.connection.once('connected');
  



  const channel = ably.channels.get('quickstart');


  /*
    Subscribe to a channel.
    The promise resolves when the channel is attached
    (and resolves synchronously if the channel is already attached).
  */
  await channel.subscribe('greeting', (message) => {
    console.log('Received a greeting message in realtime: ' + message.id)
    update_chat_room(message.data.text,message.data.name,message.id)
    
  });
  
  
  
  
  
  
  
}



connect_ably()




document.querySelector('form').addEventListener('submit', function(event) { 
  event.preventDefault(); // Prevents the form from submitting and the page from reloading 
  // Your custom logic here 
}); 

async function send_msg(){
  const channel = ably.channels.get('quickstart');
  var text = document.getElementById("input-msg").value
  
  await channel.publish('greeting', {"text":text,"name":user_name});
  document.getElementById("input-msg").value = ""
}