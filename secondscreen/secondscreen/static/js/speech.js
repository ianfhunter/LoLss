

$("svg").click(function(){
	start = new Date();
	timer = 300;

	var w = 100,
	    h = 100,
	    x = d3.scale.ordinal().domain(d3.range(3)).rangePoints([0, w], 2);

	var fields = [
	  {name: "seconds", value: 0, size: timer}
	];

	var svg = d3.selectAll("svg")
	    .attr("width", w)
	    .attr("height", h)
	  .append("svg:g")
	    .attr("transform", "translate(-10,15)");

	setInterval(function() {
	  var now = new Date();

	  fields[0].previous = fields[0].value; 
	  change = ((now.getMinutes() - start.getMinutes())*60) + now.getSeconds() - start.getSeconds();
	  fields[0].value = change;

	  var path = svg.selectAll("path")
	      .data(fields.filter(function(d) { return d.value; }), function(d) { return d.name; });

	  path.enter().append("svg:path")
	      .attr("transform", function(d, i) { return "translate(" + x(i) + ",0)"; })
	    .transition()
	      .ease("elastic")
	      .duration(750)
	      .attrTween("d", arcTween);

	  path.transition()
	      .ease("elastic")
	      .duration(750)
	      .attrTween("d", arcTween);

	  path.exit().transition()
	      .ease("bounce")
	      .duration(750)
	      .attrTween("d", arcTween)
	      .remove();

	}, 1000);


})
function arcTween(b) {
	var arc = d3.svg.arc()
	    .innerRadius(0)
	    .outerRadius(15)
	    .startAngle(0)
	    .endAngle(function(d) { return (d.value / d.size) * 2 * Math.PI; });

  var i = d3.interpolate({value: b.previous}, b);
  return function(t) {
    return arc(i(t));
  };
}