// DrawGraph
google.charts.load('current', {packages: ['corechart', 'bar']});

function DrawGraph(country, infection, death) {

  var data = google.visualization.arrayToDataTable([
    ['Country', 'Infections', 'Deaths'],
    [country, infection, death]
  ]);

  var options = {
    colors: ['#b0120a', '#ffab91'],
    chartArea: {width: '50%'},
    hAxis: {
      title: 'Number of infections and deaths'
    }
  };

  var chart = new google.visualization.BarChart(document.getElementById('chart'));
  chart.draw(data, options);

}

// GenerateOwnGraph
function GenerateOwnGraph() {

    navigator.geolocation.getCurrentPosition((position) => {

      longitude = position.coords.longitude
      latitude  = position.coords.latitude

      document.getElementById("location").innerHTML = "Latitude: " + latitude + "<br>Longitude: " + longitude;

      $.ajax({
        url: "/update_owncountry",
        type: "get",
        data: {longitude: longitude, latitude:latitude},
        success: function(response) {
          DrawGraph(response.country,response.infection, response.death);
        },
      });

    });
  
}

// GenerateSelectGraph
function GenerateSelectGraph() {

    country_dropdown = document.getElementById("country_dropdown");
    country = country_dropdown.options[country_dropdown.selectedIndex].value;

    $.ajax({
      url: "/update_selectcountry",
      type: "get",
      data: {country: country},
      success: function(response) {
        DrawGraph(country,response.infection,response.death);
      },
     });
}
