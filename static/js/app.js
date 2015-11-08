angular.module('esfd', [
    'ngRoute',
    'esfd.home',
    'esfd.search',
    'esfd.results'])
    .service('dataService', function() {
      var data = [];
      return {
        getResult: function() {
            return data;
        },
        addResult: function(result){
            var parsed = result.split("*");
            var result = {
              "Origin": parsed[0],
              "Destination": parsed[1],
              "Hotel": parsed[2],
              "Nights": parsed[3],
              "Check In": parsed[4],
              "Check Out": parsed[5],
              "Expedia": parsed[4],
              "JetBlue": parsed[5],
              "Save": parsed[6],
              "Month": parsed[7],
              "AdvanceWeeks": parsed[8]
            }
          data.push(result);
        },
        clearResult: function(result){
          data = []
        },
      }
    })
.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      otherwise({
        redirectTo: '/home'
      });
  }]);
