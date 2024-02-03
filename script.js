function runApolloExtractor() {
    var url = $('#url').val();
    var csvFileName = $('#csv_file_name').val();
    var csvLocation = $('#csv_location').val();

    // Display a loading message
    $('#statusMessage').text('Running Apollo Extractor...');

    // Send data to the server using AJAX
    $.ajax({
        type: 'POST',
        url: '/run_selenium',
        data: {
            url: url,
            csv_file_name: csvFileName,
            csv_location: csvLocation
        },
        success: function(response) {
            // Update the status message with the response from the server
            $('#statusMessage').text(response);
        },
        error: function(error) {
            // Handle errors if needed
            $('#statusMessage').text('Error occurred while running Apollo Extractor.');
        }
    });
}
