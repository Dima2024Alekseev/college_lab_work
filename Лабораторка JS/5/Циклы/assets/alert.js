let a = +prompt('Введите стоимость 1кг конфет')  
for (let i = 1.2; i <= 2; i = i + 0.2) {
    let cost = a * i;
    alert(cost.toFixed(2));
}