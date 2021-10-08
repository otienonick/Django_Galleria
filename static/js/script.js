$(function(){
    var str = '#len'; //increment by 1 up to 1-nelemnts
    $(document).ready(function(){
      var i, stop;
      i = 1;
      stop = 5; //num elements
      setInterval(function(){
        if (i > stop){
          return;
        }
        $('#len'+(i++)).toggleClass('bounce');
      }, 500)
    });
  });


const copyBtns =[... document.getElementsByClassName('copy-btn')];
console.log(copyBtns) 
copyBtns.forEach(btn => btn.addEventListener('click', ()=>{
  console.log('click');
  const imageuRL= btn.getAttribute('data-url')
  url = window.location.host;
  console.log(imageuRL)
  navigator.clipboard.writeText( url + imageuRL)
  btn.textContent = 'copied'
}))