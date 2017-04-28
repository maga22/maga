document.getElementsByClassName('j2')[0].style.color = 'red';
document.getElementsByClassName('j2')[0].style.backgroundColor = 'wheat';
var elem = document.getElementsByTagName('div');

for(var i = 0 ; i<elem.length; i++){
  elem[i].setAttribute('title','Test');
}

function butt(){
    alert('Вы нажали на кнопку.')
}
