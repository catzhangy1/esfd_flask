angular.module('esfd', [
    'ngRoute',
    'esfd.home',
    'esfd.search',
    'esfd.results',
    'esfd.notify',
    'esfd.subscribe',
    'esfd.admin',
    'esfd.game'])
    .service('dataService', function() {
      var data = [];
      var soContent = {
        senderName:"",
        senderEmail:"",
        receiverEmail:""}
      var subscribeContent = {
        name: "",
        email: "",
        phone: "",
        origin: "",
        destination: "",
        hotel_nights: 0,
        hotel_check_in_date: new Date(),
        tolerance: 0,
        max_price: 0,
      }
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
<<<<<<< HEAD
  .config(['$routeProvider',
    function($routeProvider) {
      $routeProvider.
        otherwise({
          redirectTo: '/home'
        });
    }]);
=======
.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      otherwise({
        redirectTo: '/home'
      });
  }]);
>>>>>>> ee2bfeb74bb14dd2805a6c408ce420b41594b79b
