const textBox = document.getElementById("text");
const answerDiv = document.getElementById("answerDiv");
const button = document.getElementById("button");
button.addEventListener("click", run);

function run(){
    answerDiv.innerHTML = "";
    let text = textBox.value;
    for (let index = 0; index < text.length; index++) {
        let char = text.charAt(index);
        
        if(isCharASCII(char)){
            answerDiv.innerHTML += char;
        }
        else{
            answerDiv.innerHTML += `(${char})`;
        }

    }

}

function isCharASCII(char){
    let chatCode = char.charCodeAt(0)
    if(chatCode >= 0 && chatCode <= 255){
        return true;
    }
    else{
        return false;
    }
}
