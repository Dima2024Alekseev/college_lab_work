// function info(word){
//     console.log(word + ' !');
// }

// function summa(a,b){
//     var res = a + b;
//     console.log(res);
// }

// summa(5,7);

// info('Hello World');

// function summa(arr){
//     var sum = 0;
//     for(var i=0; i < arr.length; i++)
//         sum += arr[i];
//     console.log(sum);
// }

// var array = [6,8,1];
// summa(array);

//var num = 10;//глобальная переменная

function info(){
    var num = 10; //локальная переменная
    console.log(num);
}
info();