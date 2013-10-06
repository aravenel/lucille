$(document).ready(function() {

    //Get projects when user submits form with his username
    $('#get_projects').submit(function(event){
        event.preventDefault();
        $.getJSON(
            '/get_projects',
            {'user_id': $('#user_id').val()},
            function(data){
                console.log(data);
                $.each(data, function(index, value){
                    $('#projects').append(
                        "<h3><a href='/build_gallery' class='build_gallery'>" + value.title + "</a></h3>"
                    );
                });
                $('#projects').show(400);
            }
        );
    });

    //Call the action to build the gallery
    $('#projects').on('click', 'a', function(event){
        event.preventDefault();

        //hide the projects div
        $('#projects').hide();

        //build the iframe
    });

});
