function filter() {
    // ref_tab.forEach((val)=>{if(val.)})
    $('.vulnerable:not(:contains('+$('#vulnerable').val()+')), .origin:not(:contains('+$('#origin').val()+'))').parent().hide();
}

$(document).ready(function($) {
    $(".clickable-row").click(function() {
        // window.document.location = $(this).attr("href");
        window.open($(this).attr("href"), '_blank');
    });
});
