var number = 15;
var isHasHouse = true;

if(number == 5  || isHasHouse == true) {
    console.log('Ok');
} else if(number < 10) {
    console.log('Okey');

} else if(number == 10) {
    console.log('Okey');

} else if(number>10) {
    console.log('Okey');
}

else {
    console.log('No');
}

var stroka = 'word';
switch(stroka){
    case "4" : 
    console.log('Переменанная со значением 4');
    break;
    case "word" :
        console.log("Переменная со значением word");
        break;
    default:
        console.log('Default');
        break;
}
