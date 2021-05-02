$(document).ready(function () {
    $('.sidenav').sidenav();
    $('select').formSelect();
});
$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: false,
});
$('#backButton').click(function () {
    $('.carousel').carousel('prev');
});

$('#nextButton').click(function () {
    $('.carousel').carousel('next');
});
$(document).ready(function () {
    $('.modal').modal();
});