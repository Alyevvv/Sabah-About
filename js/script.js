// TESTIMOONIALS SECTION
$(document).ready(function(){
    $("#testimonial-slider").owlCarousel({
        items:3,
        itemsDesktop:[1000,3],
        itemsDesktopSmall:[979,2],
        itemsTablet:[768,2],
        itemsMobile:[650,1],
        pagination:true,
        autoPlay:true
    });
});


//Preloader

window.onload = function() {
    let preloader = document.getElementById('preloader');
    preloader.style.display = 'none';
};
