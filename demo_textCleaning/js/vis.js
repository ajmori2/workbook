

			   
function main() {
    $.getJSON("res/freq.json",
        function (jsonData) {
			for (var i = 0; i < jsonData.length; i++) {
				// Add the graph
				var freq = jsonData[i].freq;
				var desc = jsonData[i].desc;
				
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
								   //return color.toHsl().h;
								   return d.count;
								});

				data.reverse()
				
				var margin = { top: 50,
							   left: 50,
							   right: 50,
							   bottom: 50 };
				
				// Create DOM
				var headerDOM = document.createElement("h2");
				var text = document.createTextNode(desc);
				headerDOM.appendChild(text);
				
				var divDOM = document.createElement("div");
				document.getElementById("content").appendChild(headerDOM);
				document.getElementById("content").appendChild(divDOM);
				
				
				
				
				var realW = document.getElementById("content").offsetWidth;
				
				var width = realW - margin.left - margin.right,
					height = 400 - margin.top - margin.bottom;

				// We will use a ordinal scale, allowing us to map a series of elements
				// to a range (which will be the location on the x-axis of the bar
				// graph).
				// @see: https://github.com/mbostock/d3/wiki/Ordinal-Scales
				//
				// Our domain is the names of the color, as an array.
				//   Ex: ["red", "green", "yellow", ...]
				//
				// To translate our data, which is an array of objects that contain
				// both a .color and a .count, into an array of only color names,
				// we will use _.map() to map our array into a new array.
				//
				// Our range is all the values in [0, width].
				
				var x =
				   d3.scale.ordinal()
						   .domain( data.map(function (d) { return d.color; } ) )
						   .rangeBands( [0, width], 0.1 );
						   
				var y =
				   d3.scale.linear()
						   .domain( [0, d3.max( data, function(d) { return d.count; } )] )
						   .range( [height, 0] );

				var xAxis =
				   d3.svg.axis()
						 .scale( x )
						 .orient("bottom");
				
				var yAxis =
					d3.svg.axis()
						  .scale(y)
						  .orient("left");
						  
				var svg =
				d3.select(divDOM)
				  .append("svg")
				  .attr("w", width + margin.left + margin.right)
				  .attr("h", height + margin.top + margin.bottom)
				  .style("width", (width + margin.left + margin.right) + "px")
				  .style("height", (height + margin.top + margin.bottom) + "px")
				  .append("g")
				  .attr("transform", "translate(" + margin.left + ", " + margin.top + ")")
				  ;
				  
				svg.selectAll("rect")
				  .data(data)
				  .enter()
				  
				  .append("rect")
				  .attr("x", function (d, i) { return x(d.color); } )
				  .attr("y", function (d, i) { return y(d.count); })
				  .attr("width", x.rangeBand() )
				  .attr("height", function (d) { return height - y(d.count); })
				  .style("fill", function (d) { return d.color; })
				  .style("stroke", function(d, i) { return tinycolor(d.color).darken(); })
				  .style("stroke-width", 1)
				  ;
				  
				svg.append("g")
				  .attr("class", "axis")
				  .call(yAxis)
				  ;
				  
				svg.append("g")
				  .attr("class", "axis")
				  .attr("transform", "translate(0, " + height + ")")
				  .call(xAxis)
				  ;
				  
				
			}
        })
        .fail(function (d) { alert("Failed to load JSON!"); })
    ;                              
}
