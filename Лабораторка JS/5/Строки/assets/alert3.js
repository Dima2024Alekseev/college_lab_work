let a = prompt('Введите слово', '');
let a2 = a.split('').reverse().join('');
if (a==a2) {
    alert("Слово является палиндромом")
} else{
    alert("Слово не является палиндромом")
}
