console.log("script loaded")
let name;
let age;
let password;
document.getElementById("submit").onclick= async function store(){
    fetch("/submit");
    name=document.getElementById("name").value;
    email=document.getElementById("email").value;
    password=document.getElementById("password").value;
    confirmpassword=document.getElementById("confirmpassword").value
    if(password!=confirmpassword){
        document.getElementById("error").textContent="passwords do not match";
        console.log("passwords do not match");
        return;
    }
    else if(!name || !email || !password || !confirmpassword) {
    document.getElementById("error").textContent = "Please fill all the fields.";
    return;
}
    else {
    console.log(name,age,password);
    let response=await fetch("/signup",{
        method:"POST",
        headers:{
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name:name,
            email:email,
            password:password
        })
    })
    if(response.ok){
    window.location.href = "/home";
}
}
}

