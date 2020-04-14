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

      DrawGraph("United States", 2000, 3000);

    });
}

// GenerateSelectGraph
function GenerateSelectGraph() {

    country_dropdown = document.getElementById("country_dropdown");
    country = country_dropdown.options[country_dropdown.selectedIndex].value;

    if (country=="Germany"){

      infection = 100
      death     = 200

    } else if (country=="United Stats") {

      infection = 2000
      death     = 3000

    }

    DrawGraph(country,infection, death);

 }
