let saveFile = () => {
  // Get the data from each element on the form.

  const clientcode = document.getElementById("txtclientcode");
  const assaycode = document.getElementById("txtassaycode");
  const substratetype = document.getElementById("txtsubstratetype");
  const biorep = document.getElementById("txtbiorep");
  const loaddate = document.getElementById("txtLoaddate");
  const temperature = document.getElementById("txttemperature");
  const strain = document.getElementById("txtstrain");
  const media = document.getElementById("txtmedia");
  const bacteria = document.getElementById("txtbacteria");
  const liveordead = document.getElementById("txtliveordead");
  const treatment = document.getElementById("txttreatment");
  const concentration = document.getElementById("txtconcentration");
  const solvent = document.getElementById("txtsolvent");
  const solventconcentration = document.getElementById("txtsolventconcentration");
  const technicalreplicate = document.getElementById("txttechnicalreplicate");
  const substrateid = document.getElementById("txtsubstrateid");
  const imagingdate = document.getElementById("txtimagingdate");
  const imagingtimepoint = document.getElementById("txtimagingtimepoint");
  
  


  const operator = document.getElementById("txtoperator");
  const chips = document.getElementById("txtchips");
  const startdate = document.getElementById("txtstartdate");
  const enddate = document.getElementById("txtenddate");
  const nemaprolink = document.getElementById("txtnemaprolink");
  const localdrive = document.getElementById("txtlocaldrive");






  // This variable stores all the data.
  let data =


    "ClientCode " +
    clientcode.value  +
    " \r\n " +

    "AssayCode " +
    assaycode.value  +
    " \r\n " +

    "SubstrateType " +
    substratetype.value  +
    " \r\n " +

    "BioRep " +
    biorep.value  +
    " \r\n " +

    "LoadDate " +
    loaddate.value  +
    " \r\n " +

    "Temperature " +
    temperature.value  +
    " \r\n " +

    "Strain " +
    strain.value  +
    " \r\n " +

    "Media " +
    media.value  +
    " \r\n " +

    "Bacteria " +
    bacteria.value  +
    " \r\n " +

    "Live/DeadBacteria " +
    liveordead.value  +
    " \r\n " +

    "Treatment(InsteadOfDrug) " +
    treatment.value  +
    " \r\n " +

    "Concentration " +
    concentration.value  +
    " \r\n " +

    "Solvent " +
    solvent.value  +
    " \r\n " +

    "SolventConcentration " +
    solventconcentration.value  +
    " \r\n " +

    "TechnicalReplicate " +
    technicalreplicate.value  +
    " \r\n " +

    "SubstrateID " +
    substrateid.value  +
    " \r\n " +

    "ImagingDate " +
    imagingdate.value  +
    " \r\n " +

    "ImagingTimePoint " +
    imagingtimepoint.value  +
    " \r\n " +



















    "Operator " +
    operator.value  +
    " \r\n " +

    "NumberofChips " +
    chips.value  +
    " \r\n " +

    "StartDate " +
    startdate.value  +
    " \r\n " +

    "EndDate " +
    enddate.value  +
    " \r\n " +
    
    "NemaProLink " +
    nemaprolink.value  +
    " \r\n " +

    "LocalDriveDirectory " +
    localdrive.value;


 // console.log(data); //printing form data into the console
  // Convert the text to BLOB.
  const textToBLOB = new Blob([data], { type: "text/plain" });


  















  var filename = clientcode.value+"_"+ assaycode.value+"_"+ biorep.value;
  var month = new Date(); //months from 1-12
  var month = month.getMonth() + 1;

  var day = new Date();
  var day = day.getDate();

  var year = new Date();
  var year = year.getFullYear();

  var hour = new Date();
  var hour = hour.getHours();

  var min = new Date();
  var min = min.getMinutes();

  var sec = new Date();
  var sec = sec.getSeconds();

  newdate = year +  month +  day + "_" + hour + min + sec;
  const sFileName = filename; // The file to save the data.

  let newLink = document.createElement("a");
  newLink.download = filename;

  if (window.webkitURL != null) {
    newLink.href = window.webkitURL.createObjectURL(textToBLOB);
  } else {
    newLink.href = window.URL.createObjectURL(textToBLOB);
    newLink.style.display = "none";
    document.body.appendChild(newLink);
  }






  let companies = {"Employees" : [
    {
       "userId":"ravjy", "jobTitleName":"Developer", "firstName":"Ran","lastName":"Vijay",
       "preferredFullName":"Ran Vijay","employeeCode":"H9","region":"DL","phoneNumber":"34567689",
       "emailAddress":"ranvijay.k.ran@gmail.com"
    },
    {
       "userId":"mrvjy","jobTitleName":"Developer","firstName":"Murli","lastName":"Vijay",
       "preferredFullName":"Murli Vijay","employeeCode":"A2","region":"MU",
       "phoneNumber":"6543565","emailAddress":"murli@vijay.com"
       }
    ]
 }
    
    
      



  console.log(Json.parse(companies));








  newLink.click();
};
