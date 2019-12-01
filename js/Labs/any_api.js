// USA POPULATION API

// nation level vars
let nationPop = [];

// state level vars
let allStates = [];
let statePop = [];

// NATION LEVEL
function nationData() {
    const url = "https://datausa.io/api/data?drilldowns=Nation&measures=Population";
    
    axios.get(url)
    .then(request => {
        getNationData(request);
    })
    .catch(error => console.log(error));
}
function getNationData(request) {
    for(let ele of request.data.data) {
        let addPop = ele.Population;
        nationPop.push(addPop);
    }
    console.log(nationPop);
}

// STATE LEVEL
function stateData() {
    const url = "https://datausa.io/api/data?drilldowns=State&measures=Population&year=latest";
    
    axios.get(url)
    .then(request => {
        getStateData(request);
    })
    .catch(error => console.log(error));
}
function getStateData(request) {
    for(ele of request.data.data) {
        let addState = ele.State;
        let addPop = ele.Population;

        allStates.push(addState);
        statePop.push(addPop);
    }
    console.log(allStates);
    console.log(statePop);
}

function main() {
    nationData();
    stateData();
}
main();
// DATA IN ARRAYS DONE. 
// PROCESS FOR DISPLAYING BELOW

let dropdown = document.getElementById("inputState");
let selectedState = document.getElementById("state");
let population = document.getElementById("population");


dropdown.addEventListener("click", function() {
    let state = document.querySelectorAll("option");
    for(let i = 0; i < state.length; i++) {
        state[i].addEventListener("click", function() {
            this.classList.add("pickedState");
        })
    }
    for(let i = 0; i < state.length; i++) {
        if(state[i].classList.contains("pickedState")) {
            selectedState.textContent = allStates[i] + " is ";
            population.textContent = statePop[i]

            state[i].classList.remove("pickedState");
        }
    }
})





// addEle.addEventListener("click", function() {
//     let lis = document.querySelectorAll("li");
//     for(let i = 0; i < lis.length; i++) {
//       lis[i].addEventListener("mouseover", function() {
//         this.classList.add("selected");
//       });
//       lis[i].addEventListener("mouseout", function() {
//         this.classList.remove("selected");
//       });
//       lis[i].addEventListener("click", function() {
//         this.classList.toggle("done");
//       });
//     };
//   })
  

// STATE API

// (52) […]
// ​
// 0: {…}
// ​​
// "ID State": "04000US30"
// ​​
// "ID Year": 2017
// ​​
// Population: 1050493
// ​​
// "Slug State": "montana"
// ​​
// State: "Montana"
// ​​
// Year: "2017"
// ​​
// <prototype>: Object { … }
// ​
// 1: Object { "ID State": "04000US01", State: "Alabama", "ID Year": 2017, … }
// ​
// 2: Object { "ID State": "04000US04", State: "Arizona", "ID Year": 2017, … }
// ​
// 3: Object { "ID State": "04000US05", State: "Arkansas", "ID Year": 2017, … }
// ​
// 4: Object { "ID State": "04000US06", State: "California", "ID Year": 2017, … }
// ​
// 5: Object { "ID State": "04000US08", State: "Colorado", "ID Year": 2017, … }
// ​
// 6: Object { "ID State": "04000US09", State: "Connecticut", "ID Year": 2017, … }
// ​
// 7: Object { "ID State": "04000US10", State: "Delaware", "ID Year": 2017, … }
// ​
// 8: Object { "ID State": "04000US11", State: "District of Columbia", "ID Year": 2017, … }
// ​
// 9: Object { "ID State": "04000US12", State: "Florida", "ID Year": 2017, … }
// ​
// 10: Object { "ID State": "04000US13", State: "Georgia", "ID Year": 2017, … }
// ​
// 11: Object { "ID State": "04000US15", State: "Hawaii", "ID Year": 2017, … }
// ​
// 12: Object { "ID State": "04000US16", State: "Idaho", "ID Year": 2017, … }
// ​
// 13: Object { "ID State": "04000US17", State: "Illinois", "ID Year": 2017, … }
// ​
// 14: Object { "ID State": "04000US18", State: "Indiana", "ID Year": 2017, … }
// ​
// 15: Object { "ID State": "04000US19", State: "Iowa", "ID Year": 2017, … }
// ​
// 16: Object { "ID State": "04000US20", State: "Kansas", "ID Year": 2017, … }
// ​
// 17: Object { "ID State": "04000US21", State: "Kentucky", "ID Year": 2017, … }
// ​
// 18: Object { "ID State": "04000US22", State: "Louisiana", "ID Year": 2017, … }
// ​
// 19: Object { "ID State": "04000US23", State: "Maine", "ID Year": 2017, … }
// ​
// 20: Object { "ID State": "04000US24", State: "Maryland", "ID Year": 2017, … }
// ​
// 21: Object { "ID State": "04000US25", State: "Massachusetts", "ID Year": 2017, … }
// ​
// 22: Object { "ID State": "04000US26", State: "Michigan", "ID Year": 2017, … }
// ​
// 23: Object { "ID State": "04000US27", State: "Minnesota", "ID Year": 2017, … }
// ​
// 24: Object { "ID State": "04000US28", State: "Mississippi", "ID Year": 2017, … }
// ​
// 25: Object { "ID State": "04000US29", State: "Missouri", "ID Year": 2017, … }
// ​
// 26: Object { "ID State": "04000US02", State: "Alaska", "ID Year": 2017, … }
// ​
// 27: Object { "ID State": "04000US31", State: "Nebraska", "ID Year": 2017, … }
// ​
// 28: Object { "ID State": "04000US32", State: "Nevada", "ID Year": 2017, … }
// ​
// 29: Object { "ID State": "04000US33", State: "New Hampshire", "ID Year": 2017, … }
// ​
// 30: Object { "ID State": "04000US34", State: "New Jersey", "ID Year": 2017, … }
// ​
// 31: Object { "ID State": "04000US35", State: "New Mexico", "ID Year": 2017, … }
// ​
// 32: Object { "ID State": "04000US36", State: "New York", "ID Year": 2017, … }
// ​
// 33: Object { "ID State": "04000US37", State: "North Carolina", "ID Year": 2017, … }
// ​
// 34: Object { "ID State": "04000US38", State: "North Dakota", "ID Year": 2017, … }
// ​
// 35: Object { "ID State": "04000US39", State: "Ohio", "ID Year": 2017, … }
// ​
// 36: Object { "ID State": "04000US40", State: "Oklahoma", "ID Year": 2017, … }
// ​
// 37: Object { "ID State": "04000US41", State: "Oregon", "ID Year": 2017, … }
// ​
// 38: Object { "ID State": "04000US42", State: "Pennsylvania", "ID Year": 2017, … }
// ​
// 39: Object { "ID State": "04000US44", State: "Rhode Island", "ID Year": 2017, … }
// ​
// 40: Object { "ID State": "04000US45", State: "South Carolina", "ID Year": 2017, … }
// ​
// 41: Object { "ID State": "04000US46", State: "South Dakota", "ID Year": 2017, … }
// ​
// 42: Object { "ID State": "04000US47", State: "Tennessee", "ID Year": 2017, … }
// ​
// 43: Object { "ID State": "04000US48", State: "Texas", "ID Year": 2017, … }
// ​
// 44: Object { "ID State": "04000US49", State: "Utah", "ID Year": 2017, … }
// ​
// 45: Object { "ID State": "04000US50", State: "Vermont", "ID Year": 2017, … }
// ​
// 46: Object { "ID State": "04000US51", State: "Virginia", "ID Year": 2017, … }
// ​
// 47: Object { "ID State": "04000US53", State: "Washington", "ID Year": 2017, … }
// ​
// 48: Object { "ID State": "04000US54", State: "West Virginia", "ID Year": 2017, … }
// ​
// 49: Object { "ID State": "04000US55", State: "Wisconsin", "ID Year": 2017, … }
// ​
// 50: Object { "ID State": "04000US56", State: "Wyoming", "ID Year": 2017, … }
// ​
// 51: Object { "ID State": "04000US72", State: "Puerto Rico", "ID Year": 2017, … }
// ​
// length: 52


// NATION
// {
//     "data":[
//       {
//         "ID Nation": "01000US",
//         "Nation": "United States",
//         "ID Year": 2016,
//         "Year": "2016",
//         "Population": 323127515,
//         "Slug Nation": "united-states"
//       },
//       {
//         "ID Nation": "01000US",
//         "Nation": "United States",
//         "ID Year": 2015,
//         "Year": "2015",
//         "Population": 321418821,
//         "Slug Nation": "united-states"
//       },
//       {
//         "ID Nation": "01000US",
//         "Nation": "United States",
//         "ID Year": 2014,
//         "Year": "2014",
//         "Population": 318857056,
//         "Slug Nation": "united-states"
//       },
//       {
//         "ID Nation": "01000US",
//         "Nation": "United States",
//         "ID Year": 2013,
//         "Year": "2013",
//         "Population": 316128839,
//         "Slug Nation": "united-states"
//       }
//     ],
//     "source": [
//       {
//         "measures": ["Population"],
//         "annotations": {
//           "source_name": "Census Bureau",
//           "source_description": "Census Bureau conducts surveys of the United States Population, including the American Community Survey",
//           "dataset_name": "ACS 1-year Estimate",
//           "dataset_link": "http: //www.census.gov/programs-surveys/acs/",
//           "table_id": "B01003",
//           "topic": "Diversity"
//         },
//         "name": "acs_yg_total_population_1",
//         "substitutions": [ ]
//       }
//     ]
//   }