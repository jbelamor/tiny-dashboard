$(document).ready(function($) {
    $(".clickable-row").click(function() {
        window.open($(this).attr("href"), '_blank');
    });
});
