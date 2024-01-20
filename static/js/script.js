$('.carousel-testimonial').owlCarousel({
    loop:true,
    margin:0,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            nav:true
        },
        768:{
            items:2,
            nav:false
        },
        767:{
            items:1,
            nav:false
        },
        1000:{
            items:3,
            nav:true,
            loop:false
        }
    }
})


var scrollSpy = new bootstrap.ScrollSpy(document.body, {
    target: '#navbar-example'
  })

setTimeout(function(){
    $('#message').fadeOut('slow')
},4000)