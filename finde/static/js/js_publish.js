//OPEN MODALS DATOS DE PERFIL
document.getElementById('createList-button').addEventListener('click',
    function (){
    document.querySelector('#list-modal').style.display = 'flex';
    });


// CLOSE MODALS DATOS DE PERFIL
document.querySelector('#close-listModal').addEventListener('click',
    function (){
    document.querySelector('#list-modal').style.display = 'none';
    });