function getRandomNumber(min, max) {
    return Math.floor(Math.random() * (max - min) + min)
}  
    karta = getRandomNumber(6,14);
    mast = getRandomNumber(1,4);

    switch (mast) {
        case 1:
            mast_1 = 'Черви';
          break;
          
        case 2:
          mast_1 = 'Пики';
          break;
          
        case 3:
          mast_1 ='Буби';
          break;
          
        case 4:
            mast_1 = 'Крести';
            break; 
    }




    switch (karta) {
        case 1:
          karta_1= 'шестерка';
          break;
          
        case 2:
          karta_1 = 'семерка';
          break;
          
        case 3:
          karta_1 = 'восьмерка';
          break;
          
        case 4:
            karta_1 = 'девятка';
            break;
        case 5:
            karta_1 = 'десятка';
            break;
        case 6:
            karta_1 = 'валет';
            break;
        case 7:
            karta_1 = 'дама';
            break;
        case 8:
            karta_1 = 'король';
            break;
        case 9:
            karta_1 = 'туз';
            break;
    }

    alert(karta_1 + " " + mast_1);
