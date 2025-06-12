let a = "Мама   купила мне  новые   трусы".replace(/\s{2,}/g, ' ');
alert(a.split(' ').reverse().join(' '));
