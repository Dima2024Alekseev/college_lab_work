// var text_1 = document.getElementById('text');

// text.title = 'NewText';

// console.log(text.title);

// text.style.color = 'green';
// text.style.backgroundColor = 'red';

// text.innerHTML = 'New text<br><br>HelloWorld!!!';
// document.getElementById('text').style.color = 'white';

// var spans = document.getElementsByTagName('span');
// for(var i = 0; i < spans.length; i++) {
//     console.log(spans[i].innerHTML);
// }

// var spans = document.getElementsByClassName('simple-text');
// for(var i=0; i < spans.length; i++){
//     console.log(spans[i].innerHTML);
// }


document.getElementById('main-form').addEventListener("submit", checkForm);

function checkForm(event) {
    event.preventDefault();
    var el = document.getElementById("main-form");
    var name = el.name.value;
    var pass = el.pass.value;
    var repass = el.repass.value;
    var state = el.state.value;

    // console.log(state + " - " + pass + " - " + repass);
    var fail = "";
    if(name == "" || pass == "" || state == "")
        fail = "Заполните все поля";
    else if(name.length <= 2 || name.length > 50)
        fail = "Введите корректное имя";
    else if(pass != repass)
        fail = "Пароли должны совпадать";
    else if(pass.split("$").length > 1)
        fail = "Неккоректный пароль";

    if(fail != "") {
        document.getElementById('error').innerHTML = fail;
        return false;
    } else{
        alert("Все данные корректно заполнены");
        window.location = "https://www.youtube.com/";
    }   
    }
