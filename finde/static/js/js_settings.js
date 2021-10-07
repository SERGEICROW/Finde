//OPEN MODALS
document.getElementById('imageEdit-button').addEventListener('click',
    function (){
    document.querySelector('#pic-modal').style.display = 'flex';
    });

document.getElementById('curpEdit-button').addEventListener('click',
    function (){
    document.querySelector('#curp-modal').style.display = 'flex';
    });

document.getElementById('phoneEdit-button').addEventListener('click',
    function (){
    document.querySelector('#phone-modal').style.display = 'flex';
    });

document.getElementById('addressEdit-button').addEventListener('click',
    function (){
    document.querySelector('#address-modal').style.display = 'flex';
    });


// CLOSE MODALS
document.querySelector('#close-picModal').addEventListener('click',
    function (){
    document.querySelector('#pic-modal').style.display = 'none';
    });

document.querySelector('#close-curpModal').addEventListener('click',
    function (){
    document.querySelector('#curp-modal').style.display = 'none';
    });

document.querySelector('#close-phoneModal').addEventListener('click',
    function (){
    document.querySelector('#phone-modal').style.display = 'none';
    })

document.querySelector('#close-addressModal').addEventListener('click',
    function (){
    document.querySelector('#address-modal').style.display = 'none';
    })

