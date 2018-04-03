$(function (){

    $('.search-block').on('click',function () {
        $(this).css('width','415px');
        $(this).on('mouseleave',function () {
            $(this).css('width','209px');
        });
        $(this).on('mouseenter',function () {
            $(this).css('width','415px');
        });
    })



    $('.category-card').hover(function () {
        $('.go-about').css('display','block').css('background-color','#333');
    },function () {
        $('.go-about').css('display','none').css('background-color','#333');
    })




});
