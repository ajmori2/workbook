

			   
function main() {
    $.getJSON("res/freq.json",
        function (jsonData) {
              
            var jData = jsonData[0]
            
            var data = _.map(
                           jData,
                           function(value, key) {
                           return { artist: key,
                           count: value };
                           }
                           );

            var svg = d3.select("body")
              .append("svg")
              .attr("width",2000)
              .attr("height",600)
              
            svg.selectAll("circle")
              .data(data)
              .enter()
              .append("circle")
              .attr("cx", function (d) { return d.count * 3 + 10 ;})
              .attr("cy", function (d) {return 20 })
              .attr("r", 2)
              .append("svg:title")
              .text(function(d) { return d.artist; });
              
              
              })
        .fail(function (d) { alert("Failed to load JSON!"); })
    ;                              
}
