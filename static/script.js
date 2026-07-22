console.log("script loaded")
let name;
let age;
let password;
document.getElementById("submit").onclick= async function store(){
    fetch("/submit");
    name=document.getElementById("name").value;
    age=document.getElementById("age").value;
    password=document.getElementById("password").value;
    console.log(name,age,password);
    let response=await fetch("/signup",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name:name,
            age:age,
            password:password
        })
    })
}

