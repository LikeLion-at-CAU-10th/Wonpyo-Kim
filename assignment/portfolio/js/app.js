const checkbox = document.querySelector('.checkbox');

checkbox.addEventListener('click', toggleClick);



function toggleClick(){
    document.body.classList.toggle('dark');
    document.querySelector('.navbar').classList.toggle('dark');
    document.querySelector('.nav-me').classList.toggle('dark');
    document.querySelector('.nav-stack').classList.toggle('dark');
    document.querySelector('.nav-history').classList.toggle('dark');
    console.log('Working');
}

const img1 = document.querySelector('.first');
img1.addEventListener('mouseover', mousein);
img1.addEventListener('mouseout', mouseout);

const img2 = document.querySelector('.first1')
img2.addEventListener('mouseover', mousein1);
img2.addEventListener('mouseout', mouseout1);

function mousein(){
    document.querySelector('.text').classList.add('visible');
    
}
function mouseout(){
    document.querySelector('.text').classList.remove('visible');

}
function mousein1(){
    document.querySelector('.text1').classList.add('visible');
}

function mouseout1(){
    document.querySelector('.text1').classList.remove('visible');
}