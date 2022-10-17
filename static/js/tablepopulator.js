async function printJSON() {
   const response = await fetch("C:\Users\mattj\Downloads\Infinity2.0Django_8_22\Infinity2.0Django_8_22\static\js\things.json");
   const json = await response.json();
   console.log(json);
}



var array = [["A1","B1"],
            ["A2","B2"],
            ["A3","B3"],
            ["A4","B4"],
            ["A5","B5"],],
table = document.getElementById("table");




for(var i = 0; i < array.length; i++)
{
// create a new row
var newRow = table.insertRow(table.length);
for(var j = 0; j < array[i].length; j++)
{
// create a new cell
var cell = newRow.insertCell(j);

// add value to the cell
cell.innerHTML = array[i][j];
}
}

var thing = 22
var array2=[[thing,"B1"],
            ["A2","B2"],
            ["A3","B3"],
            ["A4","B4"],
            ["A5","B5"],],
table = document.getElementById("table2");




for(var i = 0; i < array2.length; i++)
{
// create a new row
var newRow = table.insertRow(table.length);
for(var j = 0; j < array2[i].length; j++)
{
// create a new cell
var cell = newRow.insertCell(j);

// add value to the cell
cell.innerHTML = array2[i][j];
}
}














