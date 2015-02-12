

			   
function main() {
    $.getJSON("res/freq.json",
        function (jsonData) {
        	// Add the image
        	document.getElementById("img").innerHTML =
        		'<img src="' + jsonData.file + '" class="img-responsive" />';

			// Add the graph
			var freq = jsonData.freq;
			
			var data = _.map(
			   freq,
			   function(value, key) {
			      return { color: key,
			               count: value };
			   }
			);
			
			data = _.sortBy(data,
			                function (d) {
			                   var color = tinycolor(d.color);
			                   return color.toHsl().h;
			                });
			                
			var maxValue = _.max(data,
			                     function (d) {
			                       return d.count;
			                     }).count;
	
			
			data = _.first(data, 100);
			//alert( JSON.stringify(data) );
			
			var w = 400,
			    h = 400;
			
			d3.select("#freq")
			  .append("svg")
			  .attr("w", w)
			  .attr("h", h)
			  .style("height", "400px")
			  			  
			  .selectAll("rect")
			  .data(data)
			  .enter()
			  
			  .append("rect")
			  .attr("x", function (d, i) { return i * 8; } )
			  .attr("y", function (d, i) { return h - ( ((d.count / maxValue) * 400)); })
			  .attr("width", 8)
			  .attr("height", function (d) { return (d.count / maxValue) * 400; })
			  .style("fill", function (d) { return d.color; })
			  ;
/*			  
			  .style("text-align", "right")
			  .style("width", function (d) { return  + "px";})
			 // .style("height", "5px")
			  .style("background-color", function (d) { return d.color; })
			  .text( function(d) { return d.count; } );
*/			  		
			
			
        })
        .fail(function (d) { alert("Failed to load JSON!"); })
    ;                              
}
