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
                        "<h2>" + value.title + "</h2>"
                    );
                });
            }
        );
    });

});
