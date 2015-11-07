var musicMatch = angular.module('musicMatch', []);

musicMatch.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/login', {
        templateUrl: '../templates/login.html',
        controller: 'loginCtrl'
      }).
      when('/success', {
        templateUrl: '../templates/login-success.html',
        controller: 'UserDetailCtrl'
      }).
      when('/matching', {
        templateUrl: '../tamplates/match.html',
        controller: 'MatchCtrl'
      }).
      otherwise({
        redirectTo: '/'
      });
  }]);