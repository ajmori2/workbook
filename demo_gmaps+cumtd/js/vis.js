
// d3 world map code from http://techslides.com/d3-map-starter-kit

function main() {
    $.getJSON("res/schedule.json", function (jsonData) {
    
    	$.get("res/route.hbs", function (hbs) {
    		
    		var template = Handlebars.compile(hbs);
    		var html = template( {route: jsonData} );
			document.getElementById("container").innerHTML = html;
    		
    	}).fail(function (d) { alert("Failed to load HBS!"); });
		
    }).fail(function (d) { alert("Failed to load JSON!"); });
}
