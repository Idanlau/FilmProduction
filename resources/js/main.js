$(document).ready(function(){
/*// smooth scroll*/
  
  $('.nav-link').on('click',function(){
    $('html,body').animate({
      scrollTop: $($.attr(this,'href')).offset().top
    },1000);
    return false;
  });
    
  
  $('.owl-carousel').owlCarousel({
    loop:true,
    margin:300,
    items:1
})
    
   /*======Circle Progressbar START========*/
   /*==========HTML============*/
   
    
});





