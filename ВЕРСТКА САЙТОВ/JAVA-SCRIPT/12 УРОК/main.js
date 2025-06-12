// var date = new Date();

// console.log(date.getFullYear());
// console.log(date.getMonth() + 1);
// console.log(date.getMilliseconds());
// date.setHours(12);
// console.log(date.getHours());

// var arr = [5,3,2,1];
// var stroka = arr.reverse().join(',')
// console.log(arr.join(','));
// console.log(arr.sort());
// console.log(arr.reverse().join(','));
// console.log(stroka.split(','));

class Person {
    constructor(name, age, happiness){
        this.name = name;
        this.age = age;
        this.happiness = happiness;
    }
    info(){
        console.log('Человек = ' + this.name + ', Возвраст = ' + this.age + ' лет');
    }
}

var alex = new Person('Alex', 45, true);
// console.log(alex.name);
alex.info();