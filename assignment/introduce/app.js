const checkbox = document.querySelector('.checkbox');

checkbox.addEventListener('click', toggleClick);

function toggleClick(){
    document.body.classList.toggle('dark');
    
}