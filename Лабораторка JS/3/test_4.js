let a = +prompt('Введите первое значение = ');
let b = +prompt('Введите второе значение = ');
let c = +prompt('Введите третье значение = ');
var minimal = Math.min(a, b, c);
var maxmimal = Math.max(a,b,c);

x = ((a + b + c) - minimal - maxmimal);

alert( Number(x));