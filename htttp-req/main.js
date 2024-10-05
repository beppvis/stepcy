
function test_connection(){
  //testing connection
  fetch("http://127.0.0.1:5000/get-path?start=a&to=b")

  .then((message)=> {
    const message_promise = message.json();
    message_promise
    .then((data)=>{
      console.log(data["Hello"]);
    });
  })
  .catch((error)=>{
    console.log(error)
  })
  .finally(()=>{
    console.log("Ahhh")
  });

}
