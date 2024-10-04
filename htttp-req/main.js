

function test_connection(){
  req_button.addEventListener("click",()=>{

    fetch("http://0.0.0.0:8100/gamer")
    .then((message)=> {
      console.log(message)
    })
    .catch((error)=>{
      console.log(error)
    });
  
  });

}
