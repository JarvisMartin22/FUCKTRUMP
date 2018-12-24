//set variables

var Data = data;

var tbody = d3.select("tbody");

var submit = d3.select("#filter-btn");



// Use d3 to update each cell's text 
function Table_Render() {
    Data.forEach((item) => {
        var row = tbody.append("tr");
        Object.entries(item).forEach(([key, value]) => {
          var cell = tbody.append("td");
          cell.text(value);
        })
    })
};
Table_Render()

// Second Code for Search Filter through Data
function SearchFilter(input) {
    tbody.html('');
    input.forEach((item) => {
        var row = tbody.append("tr");
        Object.entries(item).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
};

 //run date search to filter through data
submit.on("click", function() {
    var date = d3.select("#datetime").property("value");
    var filtered_data = Data.filter(item => item.datetime === date);
    SearchFilter(filtered_data);
});

//data.forEach(function(AlienData) {
   // console.log(AlienData);
//});
//append one table row `tr` for each Alien object
//data.forEach(function(AlienData) {
    //console.log(AlienData);
    //var row = tbody.append("tr");
//});
//Use `Object.entries` to console.log each weather report value
//data.forEach(function(AlienData) {
   // console.log(AlienData);
   // var row = tbody.append("tr");

    //Object.entries(AlienData).forEach(function([key, value]) {
        //console.log(key, value);
        // Append a cell to the row for each value
        //     // in the weather report object
        //var cell = tbody.append("td");
  //  });
//});

// Use d3 to update each cell's text with
//  Alien values (weekday, date, high, low)
//data.forEach(function(AlienData) {
   // console.log(AlienData);
   // var row = tbody.append("tr");
   // Object.entries(AlienData).forEach(function([key, value]) {
       // console.log(key, value);
        //     // Append a cell to the row for each value
        //     // in the weather report object
       // var cell = tbody.append("td");
       // cell.text(value);
   // });
//});
//create date search to filter through data

//function searchFunction() {
    //var input, filter, ul, li, a, i;
    //input = document.getElementById('datetime');
    //filter = input.value.toUpperCase();
    //ul= document.getElementById('filters')
    //li = ul.getElementsByTagName('filter list-group-item');

    //for(i=0 ; i< li.length; i++){
        //a = li[i].getElementsByTagName('a')[0];
        //if(a.innerHTML.toLocaleUpperCase().indexOf(filter) > -1){
            //li[i].style.display = "";
        //}
       // else{
           // li[i].style.display = 'none'
       // }
    //}



//}

// Second Code for Search Filter through Data

//var AlienSearch = data;

//var submit = d3.select("#filter-btn");
//submit.on("click", function() {

    //d3.event.preventEfault();
    //var inputElement = d3.select("#datetime");
    //var inputValue = inputElement.property("value");
    //console.log(inputValue);
   // console.log(AlienSearch);
   // var filteredData = AlienSearch.filter(person => person.datetime === inputValue);
    //console.log(filteredData);



//});


