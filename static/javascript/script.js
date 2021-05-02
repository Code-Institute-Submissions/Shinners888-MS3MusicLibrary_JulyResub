$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
    $('.modal').modal();
});
//carousel
$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: false,
});

//nav-buttons carousel
$('#backButton').click(function () {
    $('.carousel').carousel('prev');
});

$('#nextButton').click(function () {
    $('.carousel').carousel('next');
});

$(".dropdown-trigger").dropdown({
    coverTrigger: false
});