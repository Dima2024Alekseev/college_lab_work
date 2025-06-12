var counter = 0;

function onclickButton(el) {
    counter++;
    el.innerHTML = 'Вы нажали на кнопку= ' + counter;
    el.style.background = 'red';
    el.style.color = 'white';
    el.style.cssText = 'border-radius: 5px; border:0; font-size: 20px; color = "red" ';
}


function On(el) {
    if(el.value=='Hello')
    alert('И тебе привет!');
    console.log(el.value);
}