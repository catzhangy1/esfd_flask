angular.module('esfd', [
    'ngRoute',
    'esfd.home',
    'esfd.search',
    'esfd.results',
    'esfd.game'])
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
              "CheckIn": parsed[4],
              "CheckOut": parsed[5],
              "Expedia": parsed[6],
              "JetBlue": parsed[7],
              "Save": parsed[8],
              "Month": parsed[9],
              "AdvanceWeeks": parsed[10]
            }
          data.push(result);
        },
        clearResult: function(result){
          data = [];
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