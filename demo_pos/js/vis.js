

			   
function main() {
    $.getJSON("res/graph.json",
        function (jsonData) {
        
        		var color = d3.interpolateHsl("yellow", "darkblue");
				
				var margin = { top: 50,
							   left: 50,
							   right: 50,
							   bottom: 50 };
								
				var realW = document.getElementById("content").offsetWidth;
				
				var width = realW - margin.left - margin.right,
					height = 600 - margin.top - margin.bottom;

        
var force = d3.layout.force()
    .charge(-300)
    //.charge(-120)
    .linkDistance(function(d) {return 60+d.wt;})
    //.linkDistance(30)
    .size([width, height]);
						  
				var svg =
				d3.select("#content")
				  .append("svg")
				  .attr("w", width + margin.left + margin.right)
				  .attr("h", height + margin.top + margin.bottom)
				  .style("width", (width + margin.left + margin.right) + "px")
				  .style("height", (height + margin.top + margin.bottom) + "px")
				  .append("g")
				  .attr("transform", "translate(" + margin.left + ", " + margin.top + ")")
				  ;
				
				force
				  .nodes(jsonData.vertices)
				  .links(jsonData.edges)
				  //.linkStrength(0.1)
				  //.linkStrength( function (d) { if (d.wt < 10) return 0; return d.wt; } )
				  .linkStrength( function (d) { return 1-1/d.wt; } )
				  .start();
      				
  var link = svg.selectAll(".link")
      .data(jsonData.edges)
      .enter()
      .append("line")
      .attr("class", "link")
      .style("stroke-width",  function(d) { return Math.sqrt(d.wt); } ); 
      //.style("stroke-width",  function(d) { if (d.wt < 5) return 0;  return Math.sqrt(d.wt); } ); 

  var node = svg.selectAll(".node")
      .data(jsonData.vertices)
      .enter()
      .append("circle")
      .attr("class", "node")
      .attr("r", 5)
      .style("fill", function (d, i, a) { return color(i / jsonData.vertices.length); })
      .call(force.drag);

  node.append("title")
      .text(function(d) { return d.text; });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
  });
				  
				
			//}
        })
        .fail(function (d) { alert("Failed to load JSON!"); })
    ;                              
}
