
function main() {
    $.getJSON("res/freq.json",
        function (jsonData) {
        	// Add the image
        	document.getElementById("img").innerHTML =
        		'<img src="' + jsonData.file + '" class="img-responsive" />';

			// Add the graph
			
        })
        .fail(function (d) { alert("Failed to load JSON!"); })
    ;                              
}
